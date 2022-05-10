class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0:2])
            
            for n in range(2,len(nums)):
                dp[n] = max(dp[n-2]+nums[n], dp[n-1])
            
            
            return dp[-1]
        
        if len(nums) <= 2:
            return max(nums)
        
        dp0 = robber(nums[1:len(nums)])
        dp1 = robber(nums[:len(nums)-1])
        
        
        return max(dp0,dp1)