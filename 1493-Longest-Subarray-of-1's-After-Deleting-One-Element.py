class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        zeroes=0
        max_ele=float("-inf")
        for j in range(len(nums)):
            if nums[j]==0:
                zeroes+=1
            while zeroes>1:
                if nums[i]==0:
                    zeroes-=1
                i+=1
            #j-i+1 is invalid because deletion of one zero +1 should not be used
            max_ele=max(max_ele,j-i)
        return max_ele
