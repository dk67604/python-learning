import time
import numpy as np
from smart_file_processor.utils import setup_file_logger

logger = setup_file_logger("metrics", "logs/main.log")

def start_metrics_dashboard(metrics_dict):
    """
    Periodically prints latency stats from metrics_dict.
    """
    logger.info("Metrics dashboard started.")
    while True:
        try:
            if 'latencies' in metrics_dict:
                latencies = list(metrics_dict['latencies'])
                if latencies:
                    arr = np.array(latencies)
                    p50 = np.percentile(arr, 50)
                    p90 = np.percentile(arr, 90)
                    p99 = np.percentile(arr, 99)
                    logger.info(f"📊 Metrics | P50: {p50:.3f}s | P90: {p90:.3f}s | P99: {p99:.3f}s")
                else:
                    logger.info("No latencies recorded yet.")
            else:
                logger.info("'latencies' key not found in metrics_dict.")
            time.sleep(2)
        except KeyboardInterrupt:
            logger.info("Metrics dashboard stopped.")
            break
