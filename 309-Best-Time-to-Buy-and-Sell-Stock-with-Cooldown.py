class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        hold=[0]*n
        rest=[0]*n
        sell=[0]*n
        hold[0]=-prices[0]
        sell[0]=0
        rest[0]=0
        for i in range(1,n):
            hold[i]=max(hold[i-1],rest[i-1]-prices[i])
            rest[i]=max(rest[i-1],sell[i-1])
            sell[i]=hold[i-1]+prices[i]
        return max(sell[n-1],rest[n-1])

        