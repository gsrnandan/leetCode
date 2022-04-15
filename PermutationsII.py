class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        seen = set()
        def perms(n, res):
            if len(n) == 1:
                return [n]
            if len(n) == 2:
                a = []
                if (n[0], n[1]) == (n[1], n[0]):
                    a = [[n[1], n[0]]]
                else:
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
                        if j not in res:
                            res.append(j)
                return res
                    
        res = []
        r = perms(nums, res)
        return r
