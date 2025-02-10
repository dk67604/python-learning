def triplet_sum_sorted(nums):
    triplets = []
    nums.sort() #Sort-in-place
    for i in range(len(nums) -2):
        # optimization: triplets consisting only positive numbers
        # will never to be sum to 0
        if nums[i] > 0:
            break
        # to avoid duplicate triplets, skip 'a' if it's same as
        # the previous
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # Find all the paira that sum to a target of '-a' (-nums[i])
        pairs = pair_sum_sorted(nums, i+1, -nums[i])
        for pair in pairs:
            triplets.append([nums[i]] + pair)
    return triplets

def pair_sum_sorted(nums, start, target):
    pairs = []
    left, right = start, len(nums) -1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1
            # To avoid duplicate '[b,c]' pairs, skip 'b' if it's the
            # same as the previous number
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif sum < target:
            left += 1
        else:
            right -= 1
    return pairs

def test_triplet_sum_sorted():
    # Test case 1: General case with multiple triplets
    nums1 = [-4, -4, -2, 0, 0, 1, 2, 3]
    result1 = triplet_sum_sorted(nums1)
    expected1 = [[-4, 1, 3], [-2, 0, 2]]
    assert result1 == expected1, f"Test case 1 failed: {result1}"

    # Test case 2: Small list with a single valid triplet
    nums2 = [0, -1, 2, -3, 1]
    result2 = triplet_sum_sorted(nums2)
    expected2 = [[-3, 1, 2], [-1, 0, 1]]
    assert result2 == expected2, f"Test case 2 failed: {result2}"

    # Test case 3: List with no triplets summing to zero
    nums3 = [1, 2, 3, 4, 5]
    result3 = triplet_sum_sorted(nums3)
    expected3 = []
    assert result3 == expected3, f"Test case 3 failed: {result3}"

    # Test case 4: All zeros (single unique triplet)
    nums4 = [0, 0, 0, 0]
    result4 = triplet_sum_sorted(nums4)
    expected4 = [[0, 0, 0]]
    assert result4 == expected4, f"Test case 4 failed: {result4}"

    # Test case 5: Large numbers with no valid triplet
    nums5 = [-100, -50, -10, 1, 5, 100, 200]
    result5 = triplet_sum_sorted(nums5)
    expected5 = []
    assert result5 == expected5, f"Test case 5 failed: {result5}"

    # Test case 6: Edge case with exactly three numbers summing to zero
    nums6 = [-1, 0, 1]
    result6 = triplet_sum_sorted(nums6)
    expected6 = [[-1, 0, 1]]
    assert result6 == expected6, f"Test case 6 failed: {result6}"

    # Test case 7: Single element (should return an empty list)
    nums7 = [0]
    result7 = triplet_sum_sorted(nums7)
    expected7 = []
    assert result7 == expected7, f"Test case 7 failed: {result7}"

    # Test case 8: Two elements (should return an empty list)
    nums8 = [0, 1]
    result8 = triplet_sum_sorted(nums8)
    expected8 = []
    assert result8 == expected8, f"Test case 8 failed: {result8}"

    print("All test cases passed successfully!")

# Run the test cases
test_triplet_sum_sorted()