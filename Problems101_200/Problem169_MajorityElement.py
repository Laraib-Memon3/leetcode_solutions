class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]


# How it works:

# Sort the array.

# The majority element will always occupy the middle position (n//2) because it appears more than half the time.

# Return that middle element.
#  Dry Run Example 1
# Input: nums = [3,2,3]

# After sort → [2,3,3]

# n = 3, n//2 = 1

# nums[1] = 3 → ✅ Output = 3.

# Dry Run Example 2
# Input: nums = [2,2,1,1,1,2,2]

# After sort → [1,1,1,2,2,2,2]

# n = 7, n//2 = 3

# nums[3] = 2 → ✅ Output = 2.