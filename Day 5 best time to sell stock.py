class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mpws=-1000000000
        mpwts=0
        for i in prices:
            mpws=max(mpws,mpwts-i)
            mpwts=max(mpwts,mpws+i)
        return mpwts
            
        
