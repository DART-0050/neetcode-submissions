class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            a = [0]*26
            for letter in word:
                i = ord(letter)-ord('a')
                a[i]+=1
            key = tuple(a)
            d[key].append(word)
        return list(d.values())
    
                

