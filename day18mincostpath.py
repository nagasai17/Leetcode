class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        k=[[0]*len(grid[0]) for i in range(len(grid))]
        k[0][0]=grid[0][0]
        for i in range(1,len(grid)):
            k[i][0]=k[i-1][0]+grid[i][0]
        for i in range(1,len(grid[0])):
            k[0][i]=k[0][i-1]+grid[0][i]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                k[i][j]=min(k[i][j-1],k[i-1][j])+grid[i][j]
        return (k[len(grid)-1][len(grid[0])-1])        
            
