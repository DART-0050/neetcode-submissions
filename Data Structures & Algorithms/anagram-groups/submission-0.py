class Solution:

    def make_dict(self, text: str) -> Dict:
        d = {}
        for letter in text:
            if letter in d:
                d[letter]+=1
            else:
                d[letter]=1
        return d
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = []
        for string in strs:
            dicts.append(self.make_dict(string))
        l = len(strs)
        ans = []
        visited = set()
        for i in range(l):
            if i in visited:
                continue
            a = [strs[i]]
            for j in range(i+1,l):
                if dicts[i]==dicts[j] and j not in visited:
                    a.append(strs[j])
                    visited.add(j)
            ans.append(a)
        return ans
                

