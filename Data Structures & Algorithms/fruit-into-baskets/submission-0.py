import collections
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        types = collections.defaultdict(int)
        curr_count = 0
        max_count = 0
        for r in range(len(fruits)):
            types[fruits[r]] += 1
            curr_count += 1

            while len(types) > 2:
                types[fruits[l]] -= 1
                curr_count -= 1

                if not types[fruits[l]]:
                    types.pop(fruits[l])

                l += 1

            max_count = max(max_count, curr_count)
        return max_count
