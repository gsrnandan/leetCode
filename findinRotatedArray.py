class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
   
        def binSearch(n, t, l, r):
            print("n, t, l, r", n, t, l, r)
            
            if r < l:
                return -1
            
            mid = (r + l)//2
            
            if t == nums[mid]:
                return mid
            
            if t > n[mid]:
                return binSearch(n, t, mid+1, r)
            else:
                return binSearch(n, t, l, mid-1)           
            return l
            
        
        if len(nums) == 1:
            if target in nums:
                return 0
            else:
                return -1
        
        rotated = False
        if nums[0] > nums[-1]:
            rotated = True
        
        if not rotated:
            return binSearch(nums, target, 0, len(nums)-1)
        
        l = 0
        r = len(nums)-1
        while (r > l) and (nums[l] > nums[r]):
            l = l+1
            r = r-1
        
        while (nums[l] > nums[l-1]):
            l = l + 1

        if target > nums[-1]:
            return binSearch(nums, target, 0, l-1)
        else:
            return binSearch(nums, target, l, len(nums)-1)
