class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans=[0]*n
        stack=[]
        prev_time=0
        for log in logs:
            func_id,status,time=log.split(':')
            func_id=int(func_id)
            time=int(time)
            if status=="start":
                #current func was running until this func started
                if stack:
                    ans[stack[-1]]+=time-prev_time
                stack.append(func_id)
                prev_time=time
            else:
                #end timestamp inclusive
                ans[stack[-1]]+=time-prev_time+1
                stack.pop()
                prev_time=time+1
        return ans