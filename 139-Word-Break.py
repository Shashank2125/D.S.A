class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n=len(s)
        wordset=set(wordDict)#avoiding duplicates in segmentation in dict
        dp=[False]*(n+1)
        dp[n]=True
        #reverse loop
        for i in range(n-1,-1,-1):
            #inverse loop
            for j in range(i+1,n+1):
                #check if string in ws and dp j is True
                if s[i:j] in wordset and dp[j]:
                    dp[i]=True
                    break
        return dp[0]
                