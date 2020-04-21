# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    
            
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        k,n=binaryMatrix.dimensions()
        k-=1
        n-=1
        r=0
        c=n
        while(r<=k and c>=0):
            if(binaryMatrix.get(r,c)==1):
                c-=1
            else:
                r+=1
        if(c==n):
            return -1
        else:
            return c+1
    

            
