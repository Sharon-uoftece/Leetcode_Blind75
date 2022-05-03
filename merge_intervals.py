 def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        ans = []
        intervals_sorted = sorted(intervals, key=lambda x: int(x[0]))
        
        minNum = intervals_sorted[0][0]
        maxNum = intervals_sorted[0][1]
        ans.append([minNum, maxNum])
        
        for i in range(1,len(intervals_sorted)):
            currMin = intervals_sorted[i][0]
            currMax = intervals_sorted[i][1]
            if currMin <= maxNum:
                maxNum = max(maxNum, currMax)
                ans.pop()
                ans.append([minNum, max(maxNum, currMax)])
            else: 
                minNum = currMin
                maxNum = currMax
                ans.append([currMin, currMax])
                
        print(intervals_sorted)
        print(ans)
        
        return ans
        