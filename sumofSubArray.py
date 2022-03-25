class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        for i in range(len(nums)):
            print("i", nums[i])
            res = 0
            for j in range(i, len(nums)):
                print("j", nums[j])
                res = res + nums[j]
                print("res", res)
                if res == k:
                    count = count+1
        
        return count
