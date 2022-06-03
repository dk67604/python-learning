from heapq import *


def find_k_frequent_numbers(nums, k):
    numFrequencyMap = dict()
    for num in nums:
        numFrequencyMap[num] = numFrequencyMap.get(num, 0) + 1

    minHeap = []
    for num, frequency in numFrequencyMap.items():
        heappush(minHeap, (frequency, num))
        if len(minHeap) > k:
            heappop(minHeap)
    topNumbers = []
    while minHeap:
        topNumbers.append(heappop(minHeap)[1])

    return topNumbers


def n_frequent_words(posting, N):
    words = posting.lower().split()
    hashmap = {}
    for word in words:
        if word in hashmap.keys():
            hashmap[word] += 1
        else:
            hashmap[word] = 1
    minHeap = []
    for word, frequency in hashmap.items():
        heappush(minHeap, (frequency, word))
        if len(minHeap) > N:
            heappop(minHeap)
    result = []
    while minHeap:
        item = heappop(minHeap)
        result.append((item[1], item[0]))
    return sorted(result, reverse=True)


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))

    posting = """
    Herbal sauna uses the healing properties of herbs in combination with distilled water.   
    The water evaporates and distributes the effect of the herbs throughout the room.   
    A visit to the herbal sauna can cause real miracles, especially for colds. 
    """
    n = 3
    print(str(n_frequent_words(posting, n)))


main()
