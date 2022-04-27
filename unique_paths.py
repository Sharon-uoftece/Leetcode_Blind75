class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = [[0] * n for i in range(m)]
        
        ans[0][0] = 1
        
        for i in range(1,m):
            ans[i][0] = 1
            
        for j in range(1,n):
            ans[0][j] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                ans[i][j] = ans[i-1][j] + ans[i][j-1]
                
        print(m,n,ans)
        
        return ans[m-1][n-1]