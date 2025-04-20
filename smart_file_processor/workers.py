import json
from smart_file_processor.utils import setup_file_logger
from multiprocessing import Lock

logger = setup_file_logger("workers", "logs/main.log")

# Global lock for safe metric updates
metrics_lock = Lock()

def process_batch(batch, metrics_dict, metrics_lock):
    """
    CPU-bound processing function that parses JSON lines and updates metrics.
    """
    latencies = []
    for line in batch:
        try:
            data = json.loads(line)
            if 'latency' in data:
                latencies.append(data['latency'])
        except json.JSONDecodeError:
            logger.warning(f"Invalid JSON line: {line}")

    if latencies:
        with metrics_lock:
            # Update total count
            total = metrics_dict.get('total', 0)
            metrics_dict['total'] = total + len(latencies)

            # Append latencies for percentile tracking
            current_latencies = list(metrics_dict['latencies'])
            current_latencies.extend(latencies)
            metrics_dict['latencies'] = current_latencies

        logger.info(f"Processed {len(latencies)} latencies in batch.")
    else:
        logger.info("Batch had no valid latencies.")
