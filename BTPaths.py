# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        if not root.left and not root.right:
            return [str(root.val)]
        
        sol = []
        def ptrav(node, curr):
            
            if not node:
                return
            
            if not node.left and not node.right:
                curr.append(str(node.val))
                sol.append("->".join(curr[:]))
                curr.pop()
                return
            
            if node != None:
                curr.append(str(node.val))
                ptrav(node.left, curr)
                ptrav(node.right, curr)
                curr.pop()
        
        ptrav(root, [])
        return sol
