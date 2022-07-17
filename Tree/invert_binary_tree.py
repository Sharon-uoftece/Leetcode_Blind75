class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
    
        
        def basicInvert(root):
            if not root:
                return
            
            temp = root.left
            root.left = root.right
            root.right = temp
            
            
            basicInvert(root.right)
            basicInvert(root.left)
            
            return root
        
        return basicInvert(root)