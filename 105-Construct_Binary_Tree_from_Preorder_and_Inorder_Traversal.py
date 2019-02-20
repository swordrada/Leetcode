# class TreeNode:
#     def __init__(self, x_:
#         self.val = x
#         self.left = None
#         self.right = None

# 递归法 
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorderr
        sep = 0
        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                sep = i
                break
        # sep = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:sep+1], inorder[:sep])
        root.right = self.buildTree(preorder[sep+1:], inorder[sep+1:])
        return root
