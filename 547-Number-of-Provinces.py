class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        visited=[False]*n
        count=0
        def dfs(node,visited):
            visited[node]=True
            for neigh in range(n):
                if not visited[neigh] and isConnected[node][neigh]==1:
                    dfs(neigh,visited)
        #for province in cities
        for i in range(n):
            #if not visited
            if visited[i]==False:
                #we can enter this so count+=1
                count+=1
                #pass the province number
                dfs(i,visited)
        return count