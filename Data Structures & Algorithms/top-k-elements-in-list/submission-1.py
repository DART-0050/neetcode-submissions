class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        sorted_keys = sorted(d.items(), key=lambda x:x[1], reverse=True)
        return [key for key,val in sorted_keys[:k]]