from typing import List

class Solution: 
    # Matt's Dictionary Approach - 124ms (Beats 78%)
    # Runtime: o(n)
    # Memory: o(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for i in nums:
            if i not in nums_dict:
                nums_dict[i] = True
            else:
                return True
        return False
    """
    # Matt's First Approach - 132ms (Beast 31%)
    # Runtime: o(n log n)
    # Memory: o(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    """

s = Solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
