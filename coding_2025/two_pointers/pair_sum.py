def pair_sum(nums,target):
    left = 0
    right = len(nums) - 1
    while (left < right):
        sum = nums[left] + nums[right]
        if (sum < target):
            left += 1
        elif (sum > target):
            right -=1
        else:
            return [left, right]
    return []


def test_pair_sum():
    nums1 = [-5, -2, 3, 4, 6]
    target1 = 7
    result1 = pair_sum(nums1,target1)
    print(result1)
    assert 2 == result1[0]
    assert 3 == result1[1]
    nums2 = [-3, -2, -1]
    target2 = -5
    result2 = pair_sum(nums2, target2)
    print(result2)
    assert 0 == result2[0]
    assert 1 == result2[1]

test_pair_sum()