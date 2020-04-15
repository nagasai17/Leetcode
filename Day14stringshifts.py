class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s=list(s)
        for i in shift:
            if(i[0]==0):
                s=s[i[1]:]+s[:i[1]]
            else:
                s=s[-i[1]:]+s[:-i[1]]
        return "".join(s)        
