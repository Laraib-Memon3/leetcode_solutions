class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
    
        n = len(nums)
        if k == 0:
            return

        k = k%n #when k> nums length
    # k = 8 and nums = 7, 8%7
        nums[:] = reversed(nums) # : means starting index, start from 0
    #reverse whole array
        nums[:k] = reversed(nums[:k]) #reverse from start up to k
        nums[k:] = reversed(nums[k:])
        return nums