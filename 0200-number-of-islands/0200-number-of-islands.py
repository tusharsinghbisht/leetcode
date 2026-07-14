class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        visited = [[False]*n for _ in range(m)]

        def dfs(i,j):
            if grid[i][j] != '1' or visited[i][j]:
                return
            visited[i][j] = True
            
            moves = [(-1,0),(1,0),(0,1),(0,-1)]
            for di, dj in moves:
                ni, nj = i+di, j+dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n:
                    dfs(ni, nj)
                    

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(i, j)

        return count