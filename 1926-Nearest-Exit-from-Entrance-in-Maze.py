from collections import deque
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m,n=len(maze),len(maze[0])
        er,ec=entrance
        queue=deque([(er,ec,0)])
        visited={(er,ec)}
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            r,c,steps=queue.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if not(0<=nr<m and 0<=nc<n):
                    continue
                if maze[nr][nc]=="+" or (nr,nc)in visited:
                    continue
                visited.add((nr,nc))
                #checking if neighbour has an exit
                if nr==0 or nr==m-1 or nc==0 or nc==n-1:
                    return steps+1
                queue.append((nr,nc,steps+1))
        return -1
                

        