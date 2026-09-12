class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        mapp={}
        for i in range(len(arr)):
            mapp[arr[i]]=mapp.get(arr[i],0)+1
        occurence=set()
        for key,value in mapp.items():
            if value in occurence:
                return False
            else:
                occurence.add(value)
        return True

        