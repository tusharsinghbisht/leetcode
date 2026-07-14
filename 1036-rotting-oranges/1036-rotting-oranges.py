class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def bfs(rottens):
            queue = deque([(r,c,0) for r,c in rottens])
            
            while queue:
                r, c, t = queue.popleft()
                moves = [(-1,0),(1,0),(0,1),(0,-1)]
                for dr, dc in moves:
                    nr, nc = r + dr, c+dc
                    if nr >= 0 and nr < m and nc >= 0 and nc < n:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            queue.append((nr, nc, t+1))
            return t

        time = float("infinity")
        rottens, fresh = [], 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rottens.append((r,c))

        if len(rottens) > 0:
            time = bfs(rottens)
            for r in range(m):
                for c in range(n):
                    if grid[r][c] == 1:
                        return -1
            return time
            
        if fresh > 0:
            return -1
        return 0
