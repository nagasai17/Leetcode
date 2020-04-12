class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsofar=0
        maxend=min(nums)
        for i in range(len(nums)):
            maxsofar+=nums[i]
            maxend=max(maxend,maxsofar)
            if(maxsofar<0):
                maxsofar=0
        return maxend        
            
        
