class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        
        prev = None
        previz = []
        newH = ListNode(0)
        curr = newH
        while list1 and list2:
            if list1.val > list2.val:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next
            else:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
        
        if list1:
            while list1:
                curr.next = ListNode(list1.val)
                curr = curr.next
                list1 = list1.next
        elif list2:
            while list2:
                curr.next = ListNode(list2.val)
                curr = curr.next
                list2 = list2.next        
        
        return newH.next
