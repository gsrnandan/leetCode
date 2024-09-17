class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lnums = [[i] for i in nums]
        def subset(nums, curr):
            tnums = []
            for i in range(len(curr)):
                for j in range(len(nums)):
                    if curr[i][-1] < nums[j]:
                        if nums[j] not in curr[i]:
                            temp = curr[i].copy()
                            temp.append(nums[j])
                            if temp not in curr:
                                tnums.append(temp)            
            curr.extend(tnums)
            if not tnums:
                curr.append(tnums)
                return curr
            return subset(nums, curr)
        return subset(nums, lnums)
