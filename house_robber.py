class Solution:
    def rob(self, nums: List[int]) -> int:
        maxMoney = [0] * len(nums)
        
        if len(nums) < 2:
            return max(nums)
        
        maxMoney[0] = nums[0]
        maxMoney[1] = nums[1]
        
        for i in range(2,len(nums)):
            maxMoney[i] = max(maxMoney[i-2]+nums[i],maxMoney[i-3]+nums[i])
            
        
        return max(maxMoney)