class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        d = {}
        for i in nums:
            if i in d :
                return True
            else:
                d[i]=1
        return False