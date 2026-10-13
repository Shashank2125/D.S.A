class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph=[[] for _ in range(n)]
        #we create a graph if it goes towards 0 we store node,0 else node,1
        for a,b in connections:
            graph[a].append((b,1))
            graph[b].append((a,0))
        visited=[False]*n
        def dfs(node):
            visited[node]=True
            count=0
            for neigh,direction in graph[node]:
                if not visited[neigh]:
                    #the graph value help us here when direction appropriate count+=0 else count+=1
                    count+=direction
                    count+=dfs(neigh)
            return count
        return dfs(0)


        