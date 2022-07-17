class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []
        q = deque()
        temp = []
        
        if root:
            q.append(root)
            
        while len(q) > 0:
            
            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    temp.append(node.val)
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        
        ans = sorted(temp)
        return ans[k-1]