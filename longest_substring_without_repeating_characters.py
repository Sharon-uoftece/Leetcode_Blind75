class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        window = s
        ans = 0
        
        for i in range(len(window)):
            if window[i] not in temp:
                temp.append(window[i])
            else:
                ans = max(ans,len(temp))
                index = temp.index(window[i])
                temp = temp[index+1:]
                temp.append(window[i])
                
        
        ans = max(ans,len(temp))
        return ans
        
                