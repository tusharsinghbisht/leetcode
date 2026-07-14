class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        target = image[sr][sc]

        if target == color:
            return image

        def dfs(i, j):
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
                moves = [(-1,0),(1,0),(0,1),(0,-1)]
                for di, dj in moves:
                    ni, nj = i + di, j+dj
                    if ni >= 0 and ni < m and nj >= 0 and nj < n:
                        if image[ni][nj] == target:
                            queue.append((ni, nj))

        # dfs(sr, sc)
        dfs(sr, sc)

        return image