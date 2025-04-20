import asyncio
import aiofiles
import os
from smart_file_processor.utils import setup_file_logger
from multiprocessing import Queue
logger = setup_file_logger("file_watcher", "logs/main.log")

async def start_async_file_reader(file_path: str, input_queue:Queue):
    """
    Asynchronously read a file line by line and put each line into the input queue.
    """
    logger.info(f"Watching file: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"File {file_path} does not exist.")
        return

    try:
        async with aiofiles.open(file_path, mode='r') as file:
            async for line in file:
                line = line.strip()
                if line:
                    logger.info(f"Read line: {line}")
                    input_queue.put(line)
                    await asyncio.sleep(0.1)  # Simulate some processing delay
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")

     # Send poison pill
    input_queue.put(None)
    logger.info(f"Finished watching file: {file_path}")