class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(len(nums)):
            p1 = nums[i]
            for j in range(len(nums)):
                if i == j:
                    continue
                p2 = nums[j]
                for k in range(j+1, len(nums)):
                    if k == i or k == j:
                        continue
                    p3 = nums[k]
                    if p1 + p2 + p3 == 0:
                        if sorted([p1, p2, p3]) not in result:
                            result.append(sorted([p1, p2, p3]))
            
        return result
      
      ******************************************************************************************************************************
      
      
