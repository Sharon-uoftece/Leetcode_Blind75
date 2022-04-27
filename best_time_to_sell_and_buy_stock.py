def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = [0] * len(prices)
        minPrice = [0] * len(prices)
        
        maxProfit[0] = 0
        minPrice[0] = prices[0]
        
        
        for p in range(1,len(prices)):
            minPrice[p] = min(prices[p],minPrice[p-1])
            maxProfit[p] = max(prices[p] - minPrice[p],maxProfit[p-1])
        
        return maxProfit[len(maxProfit)-1]