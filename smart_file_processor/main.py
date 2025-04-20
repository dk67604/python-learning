from smart_file_processor.utils import setup_file_logger
from multiprocessing import Process, Queue, Manager, Lock
from smart_file_processor.dispatcher import dispatcher_loop
from smart_file_processor.metrics import start_metrics_dashboard
from smart_file_processor.file_watcher import start_async_file_reader
import asyncio

def main():
    logger = setup_file_logger("main", "logs/main.log")
    logger.info("Initializing smart file processor pipeline...")

    input_queue = Queue()
    metrics_dict = Manager().dict()
    metrics_dict['latencies'] = []  # Initialize latencies list for metrics tracking
    metrics_lock = Lock()  # Shared lock for safe metric updates

    logger.info("Starting metrics dashboard process...")
    metrics_proc = Process(target=start_metrics_dashboard, args=(metrics_dict,), name="MetricsDashboard")
    metrics_proc.start()

    logger.info("Starting dispatcher process...")
    dispatcher_proc = Process(target=dispatcher_loop, args=(input_queue, metrics_dict, metrics_lock), name="Dispatcher")
    dispatcher_proc.start()

    logger.info("Starting asynchronous file reader...")
    try:
        asyncio.run(start_async_file_reader("data/sample.jsonl", input_queue))
    except Exception as e:
        logger.exception("Error in async file reader: %s", e)

    dispatcher_proc.join()
    metrics_proc.terminate()  # Ensure dashboard stops after dispatcher
    metrics_proc.join()

    logger.info("All components finished. Exiting.")

if __name__ == "__main__":
    main()