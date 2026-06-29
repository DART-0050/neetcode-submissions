class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]
        for i in range(len(nums)):
            subs += [subset + [nums[i]] for subset in subs]
            
        return subs
