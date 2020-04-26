class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        l=[[0]*(m+1) for i in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if(i==0 or j==0):
                    l[i][j]=0
                elif(text2[i-1]==text1[j-1]):
                    l[i][j]=l[i-1][j-1]+1
                else:
                    l[i][j]=max(l[i][j-1],l[i-1][j])
        return l[n][m]            
        
