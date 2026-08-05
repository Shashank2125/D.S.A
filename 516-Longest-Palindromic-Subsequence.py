class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        def lcs(s,rs):
            n=len(s)
            m=len(rs)
            dp=[[0]*(m+1) for _ in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if s[i-1]==rs[j-1]:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            return dp[n][m]
        rs="".join(reversed(s))
        return lcs(s,rs)
        