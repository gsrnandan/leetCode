class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def compare(s, t, replace=False):
            print("s, t", s, t)
            if not replace:
                for l in range(len(t)):
                    if s[l] != t[l]:
                        return False
                return True
            else:
                flag = False
                for l in range(len(t)):
                    if s[l] != t[l]:
                        if flag:
                            return False
                        else:
                            flag = True
                if flag:
                    return True
            return False
        
        i = 0
        j = 0
        
        if abs(len(s)-len(t)) == 1:
            if len(s) > len(t):
                for i in range(len(t)):
                    if s[i] != t[i]:
                        return compare(s[i+1:], t[i:])
                return True

            elif len(s) < len(t):
                print("in t")
                for i in range(len(s)):
                    if s[i] != t[i]:
                        return compare(s[i:], t[i+1:])
                return True
        
        elif abs(len(s)-len(t)) == 0:
            return compare(s, t, True)
        
        return False
