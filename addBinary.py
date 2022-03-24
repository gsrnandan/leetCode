class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        def btod(a):
            a = a[::-1]
            dec = 0
            for i in range(len(a)):
                bin = 0
                if a[i] == '1':
                    bin = 1
                dec += pow(2, i) * bin
            return dec

        def dtob(d):
            binary = []
            while d > 1:
                if d%2:
                    binary.append('1')
                else:
                    binary.append('0')
                d = d//2
            if d == 1:
                binary.append('1')
            else:
                binary.append('0')
            return binary
        
        add = btod(b) + btod(a)
        binary = dtob(add)
        binary = binary[::-1]
        res = ''.join(binary)
        
        return res
