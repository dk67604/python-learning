import json
import random
from pathlib import Path

def generate_sample_jsonl(filepath: str, num_records: int = 1000):
    Path(filepath).parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, 'w') as f:
        for _ in range(num_records):
            record = {
                "event": "request",
                "latency": round(random.uniform(0.1, 1.0), 3),
                "size": random.randint(100, 1000)
            }
            f.write(json.dumps(record) + "\n")

    print(f"✅ Generated {num_records} records in {filepath}")

if __name__ == "__main__":
    generate_sample_jsonl("data/sample.jsonl", num_records=1000)  # or 10_000 for larger tests
