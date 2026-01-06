class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Initialize an empty list to store indices of target
        array = []

        # If target is not present in nums, return empty list
        if target not in nums:
            return array

        # Sort the list so that target values appear in order
        nums.sort()

        # Iterate through the sorted list
        for i in range(len(nums)):
            # If current element matches target, store its index
            if nums[i] == target:
                array.append(i)

        # Return the list of indices where target occurs
        return array
