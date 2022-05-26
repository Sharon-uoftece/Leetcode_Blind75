class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #default value is set to be amount + 1, 
        #so we know whether we have a valid answer or not
        #dp = [12] * 12
        dp = [amount + 1] * (amount + 1)
        #set the first value to 0, because we do not need any coin to make $0
        dp[0] = 0
        
        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    #loop through all the coins and to find the minimum answer
                    dp[a] = min(dp[a], 1+dp[a-c])
        
        return dp[amount] if dp[amount] != amount + 1 else  -1