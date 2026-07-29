class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        parent=list(range(n))
        nums.sort()
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
                        parent[i]=j
        index=dp.index(max(dp))
        result=[]
        while parent[index]!=index:
            result.append(nums[index])
            index=parent[index]
        result.append(nums[index])
        result.reverse()
        return result
            
        