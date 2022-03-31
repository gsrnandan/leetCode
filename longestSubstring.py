class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        if k == 0:
            return 0
        
        hs = set()
        count = 0
        sub = []
        res = 0
        move = False
        
        i = 0
        while i < len(s):
            sub = []
            j = i
            move = False
            while j < len(s):
                print("j", j, "s[j]", s[j])
                if s[j] not in hs:
                    hs.add(s[j])
                    count = count+1
                    if count > k:
                        if len(sub) > res:
                            res = len(sub)
                        print("sub", sub)
                        print("res", res)
                        count = 0
                        hs = set()
                        break
                    sub.append(s[j])
                    
                else:
                    sub.append(s[j])
                    j = j+1
                    continue
                
                j = j+1
            
            if len(sub) > res:
                res = len(sub)
            
            print("j", j)
            i = i+1
            print("i", i)
        
        return res
