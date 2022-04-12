class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
                              
        def revL(head):
            prev = None
            current = head
            nT = ListNode(current.val, prev)
            prev = nT
            count = 1
            while(current.next is not None):
                val = current.next.val
                node = ListNode(val, prev)
                prev = node
                current = current.next
                count = count + 1
            nh = prev
            return nh, count
        
        rev, elems = revL(head)

        
        i = 1
        n1 = head
        while n1 and rev and i < elems:
            if (i%2 != 0):
                print("i", i)
                temp = n1.next
                revtemp = rev.next
                n1.next = rev
                rev.next = temp
                rev = revtemp
            n1 = n1.next
            
            i = i + 1
        n1.next = None
        
        return head
