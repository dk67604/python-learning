from collections import Counter

# Example HashMap (Dictionary)
nums = [4, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5]

freq_map = Counter(nums)

sorted_items = sorted(freq_map.items(), key= lambda x: x[1], reverse=True)
print(sorted_items)

'''
Sorting a HashMap by Frequency, Then by Key
If two elements have the same frequency, we can sort them by value (key).
'''
sorted_items = sorted(freq_map.items(), key= lambda x: (-x[1], x[0]))