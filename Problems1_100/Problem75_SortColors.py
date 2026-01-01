class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # l = left pointer (for placing 0s)
        l = 0
        # r = right pointer (for placing 2s)
        r = len(nums) - 1
        # i = current index we are scanning
        i = 0

        # Loop until current index crosses right pointer
        while i <= r:
            if nums[i] == 0:
                # If current element is 0, swap it to the left side
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            elif nums[i] == 2:
                # If current element is 2, swap it to the right side
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                # Decrement i to re-check the swapped element
                i -= 1

            # Move to the next element
            i += 1

        # No return needed, as the list is sorted in place