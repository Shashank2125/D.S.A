class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        mapp1={}
        mapp2={}
        for char in word1:
            mapp1[char]=mapp1.get(char,0)+1
        for char in word2:
            mapp2[char]= mapp2.get(char,0)+1
        if set(mapp1.keys())!=set(mapp2.keys()):
            return False
        if sorted(mapp1.values())!=sorted(mapp2.values()):
            return False
        return True
