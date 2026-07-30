class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def ispredecessor(shorter,longer):
            if len(longer)!=len(shorter)+1:
                return False
            i=0
            j=0
            skip=0
            while i<len(shorter) and j<len(longer):
                if shorter[i]==longer[j]:
                    i+=1
                    j+=1
                else:
                    skip+=1
                    j+=1
                    if skip>1:
                        return False
            return i==len(shorter)
        words.sort(key=len)
        n=len(words)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if ispredecessor(words[j],words[i]):
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
        

        


        