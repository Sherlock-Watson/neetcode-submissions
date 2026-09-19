class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        for num in nums:
            hashmap[num] += 1
        for i in hashmap:
            freq[hashmap[i]].append(i)
        for i in range(len(freq)):
            res.extend(freq[len(freq) - 1 - i])
            if len(res) == k:
                return res
        return []