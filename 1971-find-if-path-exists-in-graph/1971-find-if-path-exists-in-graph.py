from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph={}
        for i in range(n):
            graph[i]=[]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        q=deque()
        visited=set()
        start=source
        q.append(start)
        while len(q)>0:
            node=q.popleft()
            if node == destination:
                return True
            if node not in visited:
                visited.add(node)
                for nei in graph [node]:
                    if nei not in visited:
                        q.append(nei)
        return False

        