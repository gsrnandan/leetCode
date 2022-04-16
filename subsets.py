class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def btrack(i, cur):
            
            if len(cur) <= len(nums):
                sol.append(cur[:])
            else:
                return
            
            for j in range(i, len(nums)):
                cur.append(nums[j])
                btrack(j+1, cur)
                cur.pop()
            
        
        sol = []
        btrack(0, [])
        return sol
