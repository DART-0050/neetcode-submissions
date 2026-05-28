class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        maxl = [0]*n
        maxr = [0]*n

        maxl[0] = height[0]
        for i in range(1,n):
            maxl[i] = max(maxl[i-1],height[i])
        maxr[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            maxr[i] = max(maxr[i+1], height[i])
        res = 0
        for i in range(n):
            res += min(maxl[i], maxr[i]) - height[i]
        return res
            