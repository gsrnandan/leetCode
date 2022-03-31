class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        
        left = 0
        right = 0
        result = ""
        next_index = (left, False)
        dict_t = Counter(t)
        formed = 0
        r = len(dict_t)
        seen = {}
        
        while right < len(s):
            c = s[right] 
            seen[c] = seen.get(c, 0) + 1
            if c in dict_t:
                if not next_index[1] and right != left:
                    next_index = (right, True)
                if seen[c] == dict_t[c]:
                    formed += 1
                
            
            if formed == r:
                
                if not result:
                    result = s[left:right+1]
                elif len(s[left:right]) < len(result):
                    result = s[left:right+1]
                seen = {}
                if left == next_index[0]:
                    break
                left = next_index[0]
                next_index = (left, False)
                right = left
                formed = 0
                
            
            else:
                right = right+1
            
        return result
