class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for c in s:
            if c in hashmap1:
                hashmap1[c] += 1
            else:
                hashmap1[c] = 1
        for c in t:
            if c in hashmap2:
                hashmap2[c] += 1
            else:
                hashmap2[c] = 1
        if len(hashmap1) != len(hashmap2):
            return False
        for c in hashmap1:
            if (c not in hashmap2) or (hashmap1[c] != hashmap2[c]):
                return False
        return True