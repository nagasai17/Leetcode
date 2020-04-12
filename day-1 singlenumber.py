class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(list(set(nums)))*2 - sum(nums)
