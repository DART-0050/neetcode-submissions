class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = defaultdict(int)
        for i in range(len(numbers)):
            t = target - numbers[i]
            if h[t]:
                return [h[t], i+1]
            h[numbers[i]]= i+1
        return []