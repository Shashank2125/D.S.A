class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n=len(envelopes)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                #similar to lis nums[i]>nums[j]
                if (envelopes[j][0]<envelopes[i][0] and envelopes[j][1]<envelopes[i][1]):
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
        