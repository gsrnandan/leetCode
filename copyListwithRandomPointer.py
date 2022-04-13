class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def pll(head):
            node = head
            while node:
                print(node.val, node.random)
                node = node.next
        
        import collections
        node = head
        nr = collections.OrderedDict()
        ind = 0
        nl = {}
        start = Node(-1)
        prev = start
        while node:
            val = node.val
            rVal = node.random
            nr[node] = (val, rVal, ind)
            node = node.next
           
            nw = Node(val)
            prev.next = nw
            nw.random = None
            nl[ind] = nw
            prev = nw
            ind = ind + 1
        
        ind = 0
        for node, val in nr.items():
            nind = val[2]
            if val[1] != None:
                rind = nr[val[1]][2]                
                rnode = nl[rind]
                cnode = nl[nind]
                cnode.random = rnode
            ind = ind + 1
            
        
        print("nr", nr)       
        print("nl", nl)
         
        
        pll(start.next)
        return start.next
