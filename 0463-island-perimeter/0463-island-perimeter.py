class Solution:
    perimeter = 0
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False]*n for _ in range(m)]

        def dfs(i, j):
            if visited[i][j]:
                return 0

            visited[i][j] = True

            moves = [(0,1), (0,-1),(1,0),(-1,0)]
            nbr = 0
            for di, dj in moves:
                ni, nj = i+di, j+dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n:
                    if grid[ni][nj] == 1:
                        dfs(ni, nj)
                        nbr += 1
                        
            self.perimeter += 4-nbr

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return self.perimeter
                    
        return 0