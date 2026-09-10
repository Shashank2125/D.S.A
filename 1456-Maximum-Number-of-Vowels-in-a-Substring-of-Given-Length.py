class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels="aeiouAeiou"
        i=0
        substring=""
        max_sum=float("-inf")
        summ=0
        for j in range(len(s)):
            if s[j] in vowels:
                summ+=1
            substring+=s[j]
            if j-i+1==k:
                max_sum=max(max_sum,summ)
                if s[i] in vowels:
                    summ-=1
                i+=1
                substring=substring[1:]
        return max_sum
                


            
        