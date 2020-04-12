class Solution:
    def countElements(self, arr: List[int]) -> int:
        s=0
        s1=set(arr)
        for i in s1:
            if(i+1 in s1):
                s=s+arr.count(i)
        return s        
