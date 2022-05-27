import math


def smallest_subarray_sum(s, arr):
    min_lenth = math.inf

    for window_start in range(0, len(arr)):
        window_sum = 0
        window_end = window_start
        while window_end < len(arr):
            window_sum += arr[window_end]
            if window_sum >= s:
                min_lenth = min(min_lenth, window_end - window_start + 1)
                break
            window_end += 1
    if min_lenth == math.inf:
        return 0
    return min_lenth


def main():
    print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(167, [84, -37, 32, 40, 95])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


if __name__ == '__main__':
    main()
