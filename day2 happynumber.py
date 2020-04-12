class Solution:
    def isHappy(self, n: int) -> bool:
        l=[]
        k=list(str(n))
        
        
        while True:
            k=list(map(int,k))
            k1=list(map(lambda x: x**2,k))
            
            if(k1 in l):
                return False
            else:
                l.append(k1)
            print(l)    
            if(sum(k1)==1):
                return True
            k=str(sum(k1))
            
            
            
        
