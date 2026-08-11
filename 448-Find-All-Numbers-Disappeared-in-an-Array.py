class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n=len(nums)
        nums_set=set(nums)
        res=[]
        for i in range(1,n+1):
            if i not in nums_set:
                res.append(i)
        return res
            
        
        