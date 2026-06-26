class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        cur_max = -1
        a = [0]*len(arr)
        for i in range(len(arr),0,-1):
            a[i-1] = cur_max
            cur_max = max(cur_max, arr[i-1])
        return a