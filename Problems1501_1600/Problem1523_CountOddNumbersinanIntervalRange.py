# problem: 1523. Count Odd Numbers in an Interval Range
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].



class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2 - (low//2)

# Complexity
# Time Complexity: O(1)
# Space Complexity: O(1)