class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = float('inf')
        nums.sort()
        result = None
        for i in range(len(nums)):
            lo = i+1
            hi = len(nums)-1
            while lo < hi:
                sum_of_elements = nums[i] + nums[lo] + nums[hi]
                if abs(diff) > abs(target - sum_of_elements):
                    diff =  target - sum_of_elements
                    result = sum_of_elements
                if sum_of_elements > target:
                    hi = hi-1
                else:
                    lo = lo+1
            if diff == 0:
                break
        
        return result
