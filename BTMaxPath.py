class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        res = [root.val]
        
        def dfs(node):
            
            if not node:
                return 0
            
            # without split
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            res[0] = max(res[0], (node.val + leftMax + rightMax))
            
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
