class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = [0]*26
        l2 = [0]*26

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            index1 = ord(s[i]) - ord("a") 
            l1[index1] += 1

            index2 = ord(t[i]) - ord("a") 
            l2[index2] += 1
        
        return l1 == l2