class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mp = {}
        res = 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            max_freq = max(mp.values())
            replacements = (r - l + 1) - max_freq
            if replacements <= k:
                res = max(res, r - l + 1)
            else:
                mp[s[l]] -= 1
                l += 1

        return res
