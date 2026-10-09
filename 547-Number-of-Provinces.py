class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        visited=[False]*n
        def dfs(node):
            visited[node]=True
            for nei in range(n):
                if isConnected[node][nei]==1 and not visited[nei]:
                    dfs(nei)
        provinces=0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces+=1
        return provinces
        