class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        #we construct a graph for all the values 
        graph={}
        for i in range(len(equations)):
            a,b=equations[i]
            value=values[i]
            if a not in graph:
                graph[a]=[]
            if b not in graph:
                graph[b]=[]
            #if we want to a->b =2 else b->a=1/2
            graph[a].append((b,value))
            graph[b].append((a,1/value))
        def dfs(current,destination,product,visited):
            #if current pos is destination then return product
            if current==destination:
                return product
            visited.add(current)
            for neigh,weight in graph[current]:
                #if they are not visited then visit and product=current*weight to move to nexxt node
                if neigh not in visited:
                    result=dfs(neigh,destination,product*weight,visited)
                    if result!=-1.0:
                        return result
            return -1.0
        answer=[]
        for a,b in queries:
            #if query not in graph append -1.0 else execute the dfs
            if a not in graph or b not in graph:
                answer.append(-1.0)
            else:
                answer.append(dfs(a,b,1.0,set()))
        return answer

            


        