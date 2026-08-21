class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first=float("inf")
        second=float("inf")
        for num in nums:
            #if num=1 then first =1 next 2
            if num<=first:
                first=num
            #if num=2 then second=2 next 3
            elif num<=second:
                second=num
            #if num=3>second>first=triplet found
            else:
                return True
        return False
        