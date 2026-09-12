class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum=0
        total_sum=0
        for num in nums:
            total_sum+=num
        for i in range(len(nums)):
            right_sum=total_sum-left_sum-nums[i]
            if left_sum==right_sum:
                return i
            left_sum+=nums[i]
        return -1

        