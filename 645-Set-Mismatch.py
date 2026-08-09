class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        expected_sum=n*(n+1)//2
        actual_sum=sum(nums)
        
        seen=set()
        duplicate=-1
        for num in nums:
            if num in seen:
                duplicate=num
            else:
                seen.add(num)
        missing=expected_sum-actual_sum+duplicate
        return [duplicate,missing]
