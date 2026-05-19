class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1

        bl = [[] for i in range(len(nums)+1)]
        for key,val in count.items():
            bl[val].append(key)
        
        res=[]
        for i in range(len(nums),0,-1):
            for num in bl[i]:
                res.append(num)
                if len(res)==k:
                    return res
