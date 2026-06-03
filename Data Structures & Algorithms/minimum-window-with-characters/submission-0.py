class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or t == "":
            return ""
        tcount = {}
        wcount = {}
        for i in range(len(t)):
            tcount[t[i]] = tcount.get(t[i],0) + 1

        have = 0
        need = len(tcount)

        res_index = [-1,-1]
        res_length = float('inf')

        l = 0
        for r in range(len(s)):
            if s[r] in tcount:
                wcount[s[r]] = wcount.get(s[r],0) + 1
                if wcount[s[r]] == tcount[s[r]]:
                    have += 1
            while have == need:
                if (r - l + 1) < res_length:
                    res_index = [l,r]
                    res_length = r - l + 1
                if s[l] in tcount:
                    wcount[s[l]] -= 1
                    if wcount[s[l]] < tcount[s[l]]:
                        have -= 1
                l += 1
        l, r = res_index
        if res_length != float('inf'):
            return s[l:r+1]
        else:
            return ""
        


