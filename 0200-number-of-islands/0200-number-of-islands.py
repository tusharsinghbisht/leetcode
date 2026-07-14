class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        visited = [[False]*n for _ in range(m)]

        # def dfs(i,j):
        #     if grid[i][j] != '1' or visited[i][j]:
        #         return
        #     visited[i][j] = True
            
        #     moves = [(-1,0),(1,0),(0,1),(0,-1)]
        #     for di, dj in moves:
        #         ni, nj = i+di, j+dj
        #         if ni >= 0 and ni < m and nj >= 0 and nj < n:
        #             dfs(ni, nj)
        
        def bfs(i, j):
            queue = deque([(i, j)])
            visited[i][j] = True
            
            while queue:
                r, c = queue.popleft()
                
                moves = [(-1,0),(1,0),(0,1),(0,-1)]
                for dr, dc in moves:
                    nr, nc = r+dr, c+dc

                    if nr >= 0 and nr < m and nc >= 0 and nc < n:
                        if grid[nr][nc] == '1' and not visited[nr][nc]:
                            queue.append((nr,nc))
                            visited[nr][nc] = True
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    # dfs(i, j)
                    bfs(i, j)

        return count