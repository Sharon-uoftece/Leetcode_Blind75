class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        
        dptable = [[0]*(len2+1) for _ in range(len1+1)]

        for i in range(1,len1+1):
            for j in range(1,len2+1):
                
                    
                dptable[i][j] = max( dptable[i-1][j],
                                     dptable[i][j-1],
                                     dptable[i-1][j-1] + (1 if text1[i-1] == text2[j-1] else 0))
                
        return dptable[-1][-1]