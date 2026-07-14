class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(i, j):
            if grid[i][j] != 1 or visited[i][j]:
                return 0
            visited[i][j] = True
            area = 1
            moves = [(1,0),(-1,0),(0,1),(0,-1)]
            for di, dj in moves:
                ni,nj = i+di, j+dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n:
                    area += dfs(ni, nj)

            return area
        
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    maxArea = max(maxArea, dfs(i,j))

        return maxArea
