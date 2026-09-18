class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for (index, val) in enumerate(nums):
            if val in hashmap:
                return True
            hashmap[val] = index
        return False