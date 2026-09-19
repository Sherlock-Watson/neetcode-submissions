class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"#{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        # #5Hello#
        while i < len(s):
            if s[i] != "#":
                return []
            i += 1
            num_str = ""
            while i < len(s) and s[i] != '#':
                num_str += s[i]
                i += 1
            i += 1
            length = int(num_str)
            res.append(s[i:(i+length)])
            i += length
        return res

