class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        
        if not root:
            return []
        
        q = deque([root])
        res = []
        while q:
            rS = None
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rS = node 
                    q.append(node.left)
                    q.append(node.right)
            
            if rS:
                res.append(rS.val)
        
        return res
    
