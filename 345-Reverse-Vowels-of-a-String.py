class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels="aeiouAEIOU"
        i=0
        j=len(s)-1
        s=list(s)
        while i<=j:
            if s[i] in vowels and s[j] in vowels:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
            elif s[i] not in vowels:
                i+=1
            else:
                j-=1
        return "".join(s)

                


        