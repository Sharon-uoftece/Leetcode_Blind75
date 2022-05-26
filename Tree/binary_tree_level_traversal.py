class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque()
        
        if not root:
            return []
        else:
            q.append(root)
            
        while len(q) > 0:
            temp = []
            
            for i in range(len(q)):
                node = q.popleft()
                if node.val is not None:
                    temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(temp)
        
        return ans