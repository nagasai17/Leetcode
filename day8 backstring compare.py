class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        t=[]
        t1=[]
        for i in S:
            if(i=='#'):
                if(len(t)>0):
                    t.pop()
                
            else:
                t.append(i)
        
        for i in T:
            if(i=='#'):
                if(len(t1)>0):
                    del t1[-1]
                else:
                    continue
            else:
                t1.append(i)
        if(t==t1):
            return True
        else:
            return False
