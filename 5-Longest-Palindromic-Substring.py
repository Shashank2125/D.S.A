class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        start=0
        maxlen=1
        dp=[[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=True
        for length in range(2,n+1):
            for i in range(n-length+1):
                j=i+length-1
                if s[i]==s[j]:
                    if j-i<=2:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                    if dp[i][j] and length>maxlen:
                            start=i
                            maxlen=length
                else:
                    dp[i][j]=False
        return s[start:start+maxlen]



                
        