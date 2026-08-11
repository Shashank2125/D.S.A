class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack=[]
        res=[]
        j=0
        for i in range(1,n+1):
            stack.append(i)
            res.append("Push")
            if i == target[j]:
                j+=1
            else:
                stack.pop()
                res.append("Pop")
            if j==len(target):
                break
        return res
            


        