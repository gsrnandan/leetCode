class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            snum = nums[:i] + ['x'] + nums[i+1:]
            if target - nums[i] in snum:
                return [i, snum.index(target-nums[i])]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        hm = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hm:
                return [i, hm[val]]
            hm[nums[i]] = i
        return []
                
