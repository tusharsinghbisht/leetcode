class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        visited = [[False]*n for _ in range(m)]
        target = image[sr][sc]

        def dfs(i, j):
            if visited[i][j]:
                return 
            
            visited[i][j] = True
            image[i][j] = color
            moves = [(-1,0),(1,0),(0,1),(0,-1)]
            for di, dj in moves:
                ni, nj = i + di, j+dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n:
                    if image[ni][nj] == target:
                        dfs(ni, nj)

        def bfs(i, j):
            queue = deque([(i,j)])
            
            while queue:
                i, j = queue.popleft()
                image[i][j] = color
                visited[i][j] = True
                moves = [(-1,0),(1,0),(0,1),(0,-1)]
                for di, dj in moves:
                    ni, nj = i + di, j+dj
                    if ni >= 0 and ni < m and nj >= 0 and nj < n:
                        if image[ni][nj] == target and not visited[ni][nj]:
                            queue.append((ni, nj))

        # dfs(sr, sc)
        bfs(sr, sc)

        return image