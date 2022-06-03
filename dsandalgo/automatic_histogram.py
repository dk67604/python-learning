from typing import List, Dict
"""
Given a list of integers called dataset, write a function called automatic_histogram to automatically generate a dictionary representing a histogram of the data set with x bins uniformly distributed over the values.

Note: You should not include any bins that have zero values in them in your dictionary.

Note: Do NOT use numpy or pandas.

Example:

Input:

x = 3
dataset = [1,2,2,3,4,5]
Output:

automatic_histogram(dataset, x) -> {'1-2': 3, '3-4': 2, '5': 1}
"""
def create_value_count(A: List) -> Dict:
    val_cnt = {}
    for a in A:
        if a in val_cnt:
            val_cnt[a] += 1
        else:
            val_cnt[a] = 1
    return val_cnt


def automatic_histogram(dataset, x):
    element_count = create_value_count(dataset)

    unique_elements = list(element_count.keys())

    i = 0
    step = len(unique_elements) // x
    if len(unique_elements) % x != 0:
        step += 1
    buckets = {}
    while i < len(unique_elements):
        tup = tuple(unique_elements[i:i+step])
        buckets[tup] = 0
        i += step
    print(buckets)
    histogram = {}
    for e, count in element_count.items():
        for bucket in buckets:
            if e in bucket:
                if len(bucket) > 1:
                    bucket_str = str(min(bucket))+'-'+str(max(bucket))
                else:
                    bucket_str = str(bucket[0])
                if bucket_str in histogram:
                    histogram[bucket_str] += count
                else:
                    histogram[bucket_str] = count
                break
    return histogram
