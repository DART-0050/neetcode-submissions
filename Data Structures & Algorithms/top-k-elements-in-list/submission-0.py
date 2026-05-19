class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        sorted_data = sorted(d.items(), key=lambda x:x[1], reverse=True)
        print(sorted_data)
        return [key for key,value in sorted_data[:k]]