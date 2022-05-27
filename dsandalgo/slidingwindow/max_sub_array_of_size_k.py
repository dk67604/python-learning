def max_sub_array_of_size_k(k, arr):
    max_sum, window_sum = 0, 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end - window_start + 1 >= k:
            max_sum = max(window_sum, max_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


def main():
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


if __name__ == '__main__':
    main()
