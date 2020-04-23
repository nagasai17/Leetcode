class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        c=0
        while(m!=n):
            m=m>>1
            n=n>>1
            c+=1
        return m<<c    
