class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        # 4#neet4#code#4#love3#you
        res = []
        i = 0

        while i < len(s):
            # j = i
            # while s[j] != '#':
            #     j += 1
            # "Find the first # in string s, starting the search from index i, and store its position in j."
            j = s.index("#", i) 
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            res.append(word)
            i = j + 1 + length
        return res