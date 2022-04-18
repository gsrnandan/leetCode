class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        if not root.left and not root.right:
            return 0
        
  
        sol = [0]
        def ptrav(node):
            
            if not node:
                return 0
            
            if not node.left and not node.right:
                return 1
            
            ll = ptrav(node.left)
            rl = ptrav(node.right)
            mp = ll + rl
            
            sol[0] = max(sol[0], mp)
            return max(ll, rl) + 1
        
        ptrav(root)
        return sol[0]
