class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n=len(s)
        m=len(t)
        dp=[[0]*(m+1) for _ in range(n+1)]
        #starting chars =1
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1]==t[j-1]:#because we are counting number of possibilities #take  + skip
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    #skip
                    dp[i][j]=dp[i-1][j]
        return dp[n][m]       