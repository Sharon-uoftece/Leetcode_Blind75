class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return Solution.validBST(root)
    
    def validBST(node, low=-math.inf, high=math.inf):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        
        return (Solution.validBST(node.left,low, node.val) and
                Solution.validBST(node.right,node.val,high))