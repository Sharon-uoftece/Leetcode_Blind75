class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        mx, mn = ans, ans
        
        for n in range(1,len(nums)):
            if nums[n] < 0:
                mx, mn = mn, mx
            
            mx = max(nums[n]*mx, nums[n])
            mn = min(nums[n]*mn, nums[n])
            
            ans = max(mx,ans)
            
        return ans