class Solution:
    def maximalSquare(self, m: List[List[str]]) -> int:
        ma=0
        if(m==[]):
            return 0
        dp=[[None]*(len(m[0])+1)  for i in range(len(m)+1)]
        for i in range(len(m)+1):
            for j in range(len(m[0])+1):
                if(i==0 or j==0):
                    dp[i][j]=0
                elif(m[i-1][j-1]=='1'):
                    dp[i][j]=min((dp[i][j-1]),int(dp[i-1][j-1]),int(dp[i-1][j]))+1
                    ma=max(ma,dp[i][j])
                else:
                    dp[i][j]=0
        return ma*ma            
                    
        
