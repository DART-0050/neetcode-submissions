class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        d = {}
        l = len(nums)
        for i in range(l):
            if nums[i] in d :
                return True
            else:
                d[nums[i]]=1
        return False