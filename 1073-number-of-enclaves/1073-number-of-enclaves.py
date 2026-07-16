class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]

        def dfs(r, c):
            if visited[r][c]:
                return

            visited[r][c] = 1
            moves = [(0, -1), (0, 1), (-1, 0), (1,0)]
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                    if grid[nr][nc] == 1 and not visited[nr][nc]:
                        dfs(nr, nc)

        for i in range(rows):
            if grid[i][0]:
                dfs(i, 0)
            if grid[i][cols-1]:
                dfs(i, cols - 1)

        for j in range(cols):
            if grid[0][j]:
                dfs(0, j)
            if grid[rows-1][j]:
                dfs(rows-1,j)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1

        return count