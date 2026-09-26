# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        sums=[]
        def dfs(node,sums,depth):
            if node is None:
                return
            if depth==len(sums):
                sums.append(0)
            sums[depth]+=node.val
            dfs(node.left,sums,depth+1)
            dfs(node.right,sums,depth+1)
        dfs(root,sums,0)
        #if at level 3=8+7=15 arr is 0 indexed so index of 15 is 2+1=3 max level
        return sums.index(max(sums))+1
            
            
        