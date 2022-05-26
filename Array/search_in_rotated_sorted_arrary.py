class Solution:
    ans = -1
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1 and nums[0] != target:
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        pivot = self.pivotHelper(nums,0,len(nums)-1)
        
        # o(n) way to find pivot
        # for i in range(1,len(nums)):
        #     if nums[i] > nums[pivot]:
        #         pivot = i
        
        if pivot == -1:
            self.binarySearch(nums,target,0,len(nums)-1)     
        elif pivot >= 0:
            if target == nums[0]:
                return 0
            elif target < nums[0]:
                self.binarySearch(nums,target,pivot+1,len(nums)-1)
            elif target > nums[0]:
                self.binarySearch(nums,target,1,pivot)
        
        return self.ans
    
    def pivotHelper(self,nums:List[int],start,end): 
        
        if nums[0] < nums[len(nums)-1]:
            return -1
        
        if nums[0] > nums[1]:
            return 0
        
        if nums[len(nums)-2] > nums[len(nums)-1]:
            return len(nums)-2
            
                
        # if start == end:
        #     pivot = nums[start]
        #     return
        
        while start <= end:
            midIndex = int((start+end)/2)
            prevVal = nums[midIndex-1]
            curr = nums[midIndex]
            nextVal = nums[midIndex+1]
            
            if prevVal > curr and nextVal > curr:
                return midIndex - 1
                
            if prevVal < curr and nextVal < curr:
                return midIndex
                
            elif curr < nums[0]:
                end = midIndex - 1
            elif curr > nums[0]:
                start = midIndex + 1
                
    def binarySearch(self, nums: List[int], target, start, end):
        if start == end:
            if nums[end] == target:
                self.ans = end
            else:
                self.ans = -1
        
        while start <= end:
            midIndex = int((start+end) / 2)
            
            if nums[midIndex] == target:
                self.ans = midIndex
                return
            elif nums[midIndex] < target:
                start = midIndex + 1
            elif nums[midIndex] > target:
                end = midIndex - 1