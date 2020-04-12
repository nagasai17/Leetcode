class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)-nums.count(0)):
            if(nums[i]==0):
                z=0
                j=i
                while(nums[j]==0 and j<len(nums)):
                    z=z+1
                    j=j+1    
                nums[i],nums[z+i]=nums[z+i],nums[i]
        
