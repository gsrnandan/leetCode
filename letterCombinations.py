class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        dp = {'2' : ["a", "b", "c"],
              '3' : ["d", "e", "f"],
              '4' : ["g", "h", "i"],
              '5' : ["j", "k", "l"],
              '6' : ["m", "n", "o"],
              '7' : ["p", "q", "r", "s"],
              '8' : ["t", "u", "v"],
              '9' : ["w", "x", "y", "z"],
        }
        
        result = []
        
        if len(digits) == 1:
            return dp[digits[0]]
        
        if not digits:
            return []
        
        def adds(a, b):
            return a+b
        
        def perms(a, b):
            res = []
            for j in a:
                for i in b:
                    res.append(adds(j, i))
            return res
        
        res = dp[digits[-1]]
        for i in reversed(range(len(digits)-1)):
            res = perms(dp[digits[i]], res)
            
        
        return res
