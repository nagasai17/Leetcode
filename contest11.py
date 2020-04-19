class Solution:
    def reformat(self, s: str) -> str:
        s1=[str(i) for i in range(0,10)]
        l=[]
        l1=[]
        l3=[]
        for i in s:
            if(i in s1):
                l.append(i)
            else:
                l1.append(i)
        
        if(len(l1)-len(l)<=1 and len(l1)-len(l)>=0 ):
            for i in range(len(l)):
                l3.append(l1[i])
                l3.append(l[i])
            if(len(l1)-len(l)==1):
                l3.append(l1[-1])
            return "".join(l3)    
        if(len(l)-len(l1)<=1 and len(l)-len(l1)>=0):
            for i in range(len(l1)):
                l3.append(l[i])
                l3.append(l1[i])
            
            if(len(l)-len(l1)==1):
                l3.append(l[-1])
            
            return "".join(l3)
        else:
            return("")
    
        
        
