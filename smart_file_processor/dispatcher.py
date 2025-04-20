import json
from multiprocessing import Process, Queue, current_process
from smart_file_processor.utils import setup_file_logger
from smart_file_processor.workers import process_batch

logger = setup_file_logger("dispatcher", "logs/main.log")

def dispatcher_loop(input_queue: Queue, metrics_dict, metrics_lock):
    """
    Dispatcher that pulls lines from the input_queue and sends batches to worker processes.
    """
    batch_size = 10
    batch = []
    worker_processes = []

    logger.info("Dispatcher loop started.")
    poison_pills_received = 0
    expected_poison_pills = 1  # adjust this depending on how many you send

    while True:
        try:
            line = input_queue.get(timeout=5)
            if line is None:
                poison_pills_received += 1
                logger.info("Dispatcher received poison pill.")
                if poison_pills_received >= expected_poison_pills:
                    logger.info("All poison pills received. Shutting down.")
                    break
                continue

            batch.append(line)
            if len(batch) >= batch_size:
                p = Process(target=process_batch, args=(batch.copy(), metrics_dict, metrics_lock))
                p.start()
                worker_processes.append(p)
                batch.clear()
        except Exception as e:
            logger.warning(f"Dispatcher timeout or error: {e}")

    if batch:
        p = Process(target=process_batch, args=(batch.copy(), metrics_dict, metrics_lock))
        p.start()
        worker_processes.append(p)
        batch.clear()

    for p in worker_processes:
        p.join()

    logger.info("Dispatcher loop terminated.")