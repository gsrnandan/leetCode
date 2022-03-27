class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        INT_MAX = pow(2,31) - 1 
        INT_MIN = -pow(2,31)
        
        s = s.strip()
        negetive = False
        i = 0
        result = 0
        if not s:
            return result
        if s[0] == '-':
            negetive = True
            i = 1
        elif s[0] == '+': 
            negetive = False
            i = 1
        elif ord(s[0]) >= 48 and ord(s[0]) <= 57:
            negetive = False
        
        j = i
        nums = s[i:len(s)]
        while j < len(s):
            if s[j] == ' ' or ord(s[j]) < 48 or ord(s[j]) > 57:
                break
            j = j+1
        nums = s[i:j]
        
        for num in nums:
            val = ord(num) - 48
            print("val, val")
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and val > INT_MAX % 10)):
                # If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.    
                return INT_MAX if not negetive else INT_MIN
            result = 10 * result + val
            print("result ", result)

            
        if negetive:
            return -abs(result)
        return result
