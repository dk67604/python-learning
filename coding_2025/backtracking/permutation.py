def find_all_permutations(nums: List[int]) -> List[List[int]]:
    res = []
    
    def backtrack(candidates:List[int], used:Set[int]):
        nonlocal res
        if len(candidates) == len(nums):
            res.append(candidates[:])
            return
        for num in nums:
            if num not in used:
                candidates.append(num)
                used.add(num)
                backtrack(candidates, used)
                candidates.pop()
                used.remove(num)
        

    backtrack([], set())
    return res