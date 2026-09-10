class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=0
        max_ones=float("-inf")
        ones=0
        window=0
        zero=0
        for j in range(len(nums)):
            if nums[j]!=1:
                zero+=1
            while zero>k:
                if nums[i]==0:
                    zero-=1
                i+=1
            max_ones=max(max_ones,j-i+1)
        return max_ones
                       

        