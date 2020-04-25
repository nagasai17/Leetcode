class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastgoodone=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if(i+nums[i]>=lastgoodone):
                lastgoodone=i
        return lastgoodone==0        
