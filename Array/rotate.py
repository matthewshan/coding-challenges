from typing import List

class Solution:
    # Cyclic Replacements - 60ms (Beats 81%)
    # Runtime: o(n)
    # Space: o(1)
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length

        start = count = 0
        while count < length:
            i, value = start, nums[start]
            while True:
                next_i = (i + k) % length
                nums[next_i], value = value, nums[next_i]
                i = next_i
                count += 1

                if start == i:
                    break
            start += 1
        return nums
    """
    # Matt's First Approach - 60ms (Beats 81%)
    # Runtime: o(n)
    # Space: o(n)
    def rotate(self, nums: List[int], k: int) -> None:
        \"""
        Do not return anything, modify nums in-place instead.
        \"""
        length = len(nums)
        if length >= 2:
            pivot = (length - k) % length 
            result = [nums[pivot]]
            
            i = (pivot+1)%length
            while i != pivot:
                result.append(nums[i])
                i = (i + 1) % length 

            for j in range(length):
                nums[j] = result[j]
        #==============================
        return nums
    """

s = Solution()
print("Expected: [5,6,7,1,2,3,4] Actual: ", s.rotate([1,2,3,4,5,6,7], 3))
print("Expected: [3,99,-1,-100] Actual: ", s.rotate([-1,-100,3,99], 2))
print("Expected: [0] Actual: ", s.rotate([0], 1))
print("Expected: [2, 0, 1] Actual: ", s.rotate([0, 1, 2], 1))
print("Expected: [1, 2] Actual: ", s.rotate([1, 2], 0))
