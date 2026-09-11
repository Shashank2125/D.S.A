class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        prefix=[0]
        for i in range(len(gain)):
            prefix.append(prefix[i]+gain[i])
        max_so_far=0
        for i in range(len(prefix)):
            max_so_far=max(prefix[i],max_so_far)
        return max_so_far


            
        