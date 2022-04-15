class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        seen = []
        def perms(n, res):
            
            if len(n) == 1:
                return [n]
            if len(n) == 2:
                a = [[n[0], n[1]], [n[1], n[0]]]
                return a
            else:
                for i in range(len(n)):
                    elem = n[i]
                    intres = []
                    rest = n[:i] + n[i+1:]
                    a = perms(rest, intres)
                    for j in a:
                        j.append(elem)
                    res.extend(a)
                return res
                    
        res = []
        r = perms(nums, res)
        return r
