class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n=len(matrix)
        m=len(matrix[0])
        max_s=0
        dp=[[0]*(m)for _ in range(n)]
        for i in range(n):
            dp[i][0]=int(matrix[i][0])
            max_s=max(dp[i][0],max_s)
        for j in range(m):
            dp[0][j]=int(matrix[0][j])
            max_s=max(dp[0][j],max_s)
        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]=='1':
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    max_s=max(max_s,dp[i][j])
                else:
                    dp[i][j]=0
        return max_s*max_s
        