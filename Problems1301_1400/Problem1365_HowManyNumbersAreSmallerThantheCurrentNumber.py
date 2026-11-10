class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []

        for i in nums:
            counter = 0
            for j in nums:
                if j < i: 
                    counter+=1
            ans.append(counter)

        return ans

# Complexity
# Time Complexity: O(n²) - Two nested loops compare each element with all other elements.
# Space Complexity: O(n) - Extra space is used for the output array.