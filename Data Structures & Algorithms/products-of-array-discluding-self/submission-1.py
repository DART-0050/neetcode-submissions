class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        for num in nums:
            if num:
                prod = prod*num
            else:
                zeros+=1
        out = [0]* len(nums)
        if zeros >1 :
            return out
        for i in range(len(nums)):
            curr = nums[i]
            if zeros:
                out[i]=0 if curr else prod
            else:
                out[i]=prod//nums[i]
        return out