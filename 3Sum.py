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
      
      
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sunOfPairs = {}
        result = []
        val = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i == j:
                    continue
                sum_i_j = nums[i] + nums[j] 
                if sum_i_j in sunOfPairs:
                    sunOfPairs[sum_i_j].append((i, j))
                else:
                    sunOfPairs[sum_i_j] = [(i, j)]
        
        print("sunOfPairs", sunOfPairs)
        
        for i in range(len(nums)):
            key = val - nums[i]
            print("key", val - key)
            if key in sunOfPairs.keys():
                indicesPair = sunOfPairs[key]
                for indices in indicesPair:
                    if i != indices[0] and i != indices[1]:
                        print("indices", nums[indices[0]], nums[indices[1]])
                        if sorted([nums[i], nums[indices[0]], nums[indices[1]]]) not in result:
                            result.append(sorted([nums[i], nums[indices[0]], nums[indices[1]]]))
                   # result.append([nums[i], nums[sunOfPairs[key][0]], nums[sunOfPairs[key][1]]])
        
        return result
    *********************************************************************************************************
    
    class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sunOfPairs = {}
        result = []
        val = 0
        nums.sort()
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1, len(nums)):
                sum_i_j = -nums[i] - nums[j]
                if sum_i_j in seen:
                    #if nums.index(sum_i_j) != i and nums.index(sum_i_j) != j:
                    if sorted([sum_i_j, nums[i], nums[j]]) not in result:
                        result.append(sorted([sum_i_j, nums[i], nums[j]]))
                seen.add(nums[j])
        return result
        
