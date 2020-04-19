class Solution:
    def helper(self,i,j,r,c,grid):
        if(grid[i][j]=="0"):
            return 
        grid[i][j]="0"
        if(i!=0):
            self.helper(i-1,j,r,c,grid)
        if(i!=r-1):
            self.helper(i+1,j,r,c,grid)
        if(j!=0):
            self.helper(i,j-1,r,c,grid) 
        if(j!=c-1):
            self.helper(i,j+1,r,c,grid)   
        return grid    
    def numIslands(self, grid: List[List[str]]) -> int:
        c1=0
        if(grid==[]):
            return 0
        r=len(grid)
        c=len(grid[0])
        for i in range(r):
            for j in range(c):
                if(grid[i][j]=="1"):
                    self. helper(i,j,r,c,grid)
                    c1+=1
        return c1
