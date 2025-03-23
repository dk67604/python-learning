from typing import List

# Binary search to find the maximum height H at which to cut wood
def cutting_wood(heights: List[int], k: int) -> int:
    # Search range for height H: from 0 up to the tallest tree
    left, right = 0, max(heights)

    while left < right:
        # Use upper mid to avoid infinite loop when left + 1 == right
        mid = (left + right) // 2 + 1

        # Check if cutting at height 'mid' yields at least k units of wood
        if cuts_enough_wood(mid, k, heights):
            left = mid  # Try a higher cut, maybe still enough wood
        else:
            right = mid - 1  # Not enough wood, lower the cut height

    # When loop ends, right == left and is the maximum valid cut height
    return right

# Helper function to determine if cutting at height H yields enough wood
def cuts_enough_wood(H: int, k: int, heights: List[int]) -> bool:
    wood_collected = 0

    for height in heights:
        if height > H:
            # Only collect wood from parts above cut height
            wood_collected += (height - H)

    # Return True if we've collected at least k units of wood
    return wood_collected >= k
