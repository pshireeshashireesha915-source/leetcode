class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        column=len(grid[0])
        visited=[]
        for i in range(row):
            visited.append([0]*column)
        count = 0
        for i in range(row):
            for j in range(column):
                if grid[i][j] == "1" and  visited[i][j]==0:
                    self.bfs(grid,visited,i,j)
                    count+=1
        return count
    def bfs(self,grid,visited,i,j):
        row=len(grid)
        column=len(grid[0])
        q=deque()
        q.append((i,j))
        visited[i][j]=1
        while q:
            i,j=q.popleft()
            visited[i][j]=1
            if i-1>=0 and grid[i-1][j] == "1" and visited[i-1][j]==0:
                q.append((i-1,j))
                visited[i-1][j]=1
            if j+1<column and grid[i][j+1] == "1" and visited[i][j+1]==0:
                q.append((i,j+1))
                visited[i][j+1]=1
            if i+1<row and grid[i+1][j] == "1" and visited[i+1][j]==0:
                q.append((i+1,j))
                visited[i+1][j]=1
            if j-1>=0 and grid[i][j-1] == "1" and visited[i][j-1]==0:
                q.append((i,j-1))
                visited[i][j-1]=1
            

