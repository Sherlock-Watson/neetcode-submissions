class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for (index, num) in enumerate(nums):
            if (target - num) in hashmap:
                if hashmap[target - num] != index:
                    return [hashmap[target - num], index]
            hashmap[num] = index
        return []