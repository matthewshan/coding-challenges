from typing import List

class Solution:
    """
    # XOR - 92ms (Beats 43%)
    # Runtime: o(n)
    # Memory: o(1)
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result

    """
    # With Dictionary - 84ms (Beats 83%)
    # Runtime: o(n)
    # Memory: o(n)
    def singleNumber(self, nums: List[int]) -> int:
        values = {}
        for i in nums:
            if i not in values:
                values[i] = 1
            else:
                values[i] += 1
        for key, value in values.items():
            if value == 1:
                return key

s = Solution()
print(s.singleNumber([2,2,1]))
print(s.singleNumber([4,1,2,1,2]))