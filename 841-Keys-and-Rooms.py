class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n=len(rooms)
        visited=[0]*n
        def dfs(node,visited):
            visited[node]=True
            for neigh in rooms[node]:
                if not visited[neigh]:
                    dfs(neigh,visited)
        dfs(0,visited)
        return all(visited)
        