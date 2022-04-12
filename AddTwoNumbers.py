class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        print( l1)
        print( l1.val)
        
        num1 = l1
        num2 = l2
        carry = 0
        nums3 = []
        while num1 and num2:
            val = num1.val + num2.val
            if carry:
                val = val + carry
                carry = 0
            if val >= 10:
                carry = 1
                val = val%10

            nums3.append(val)           
            num1 = num1.next
            num2 = num2.next
        
        # rest of list
        rest = None
        if num1:
            rest = num1
        elif num2:
            rest = num2

        if rest:
            while rest:
                val = rest.val
                if carry:
                    val = val+carry
                    carry = 0
                if val >= 10:
                    carry = 1
                    val = val%10
                nums3.append(val)
                rest = rest.next
        
        if carry == 1:
            nums3.append(carry)
   
        head = ListNode(nums3[0])
        prev = head
        for i in range(1 , len(nums3)):
            node = ListNode(nums3[i])
            prev.next = node
            prev = node
        
        return head
