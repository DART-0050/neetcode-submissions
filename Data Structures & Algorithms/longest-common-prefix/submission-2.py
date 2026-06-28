class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        j = 0
        strs.sort()
        res = ""
        while i < len(strs[0]) and j < len(strs[-1]):
            if strs[0][i] == strs[-1][j]:
                res += strs[0][i]
                i+=1
                j+=1
            else:
                break
        return res