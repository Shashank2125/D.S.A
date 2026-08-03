class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        #lcs will give us solution ex word1=sea and word2=eat 
        #then lcs will be ea=2 chars
        def lcs(word1,word2):
            n=len(word1)
            m=len(word2)
            dp=[[0]*(m+1) for _ in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if word1[i-1]==word2[j-1]:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            return dp[n][m]
        LCS=lcs(word1,word2)
        #we suppose 3+3-2*2=6-4=2 ans for eat and sea
        return len(word1)+len(word2)-2*LCS
        