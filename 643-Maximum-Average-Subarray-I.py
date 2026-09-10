class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i=0
        max_sum=float("-inf")
        window_sum=0
        for j in range(len(nums)):
            window_sum+=nums[j]
            if j-i+1==k:
                #process current window
                max_sum=max(max_sum,window_sum)
                window_sum-=nums[i]
                i+=1
                
        return float(max_sum)/k

        