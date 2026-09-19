class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        sorted_hashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True)).keys()
        return list(sorted_hashmap)[:k]