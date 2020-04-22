from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter=Counter()
        s=0
        c=0
        counter[0]=1
        for i in nums:
            s+=i
            c+=counter[s-k]
            counter[s]+=1
        return c    
