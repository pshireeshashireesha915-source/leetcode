class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph={}
        for i in  range(len(isConnected)):
            graph[i]=[]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    graph[i].append(j)
        visited=set()
        count=0
        for i in range(len(isConnected)):
            if i not in visited:
                count+=1
                q=deque()
                q.append(i)

                while q:
                    node=q.popleft()
                    visited.add(node)
                    for nei in graph[node]:
                        if nei not in visited:
                            q.append(nei)
        return count