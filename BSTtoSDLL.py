class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if not root:
            return 
        
        if not root.left and not root.right:
            root.left = root
            root.right = root
            return root
        
        def ilist(root, r):
            for i in range(len(r)):
                root = root.right
        
        
        p = []
        r = []
        def itrav(node):
            
            if node == None:
                return
            
            if node != None:
                itrav(node.left)
                p.append(str(node.val))
                r.append(node)
                itrav(node.right)
                    
         
        
        itrav(root)
        head = None
        print("r", r)
        if len(r) == 1:
            return root
        for i in range(len(r)):
            cur = r[i]
            if i == 0:
                cur.left = r[-1]
                cur.right = r[1]
                head = cur
                continue
            if i == len(r)-1:
                cur.right = r[0]
                cur.left = r[-2]
                continue

            cur.right = r[i+1]
            cur.left = r[i-1]
   

        return head
