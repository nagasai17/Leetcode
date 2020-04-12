import bisect
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l=sorted(stones)
        while(len(l)>1):
            k=l.pop()
            k2=l.pop()
            if(k-k2>0):
                bisect.insort_left(l,k-k2)
        if(l):
            return l[0]
        else:
            return 0
                
        
