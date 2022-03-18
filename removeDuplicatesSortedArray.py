class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arrayLength = len(nums)
        
        
        for i in reversed(range(arrayLength)):
            if len(nums) == 1:
                    break
            if nums[i] == nums[i-1]:
                nums.pop(i)
        
        return len(nums)
