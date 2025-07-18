class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        array=[]
        if target not in nums:
            return array
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                array.append(i)
        return array