class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farMost = [0] * len(nums)
        
        if len(nums) <= 1:
            return True
        
        farMost[0] = nums[0]
        
        
        for f in range(1, len(farMost)):
            if farMost[f-1] >= f:
                farMost[f] = max(farMost[f-1], f+nums[f])
              
                if farMost[f] >= len(nums) - 1:
            
                    return True
                    break
 
        return False