class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            l = [0] * 26
            for c in s:
                l[ord(c) - ord('a')] += 1
            key = ",".join([str(c) for c in l])
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key] = [s]
        return list(hashmap.values())