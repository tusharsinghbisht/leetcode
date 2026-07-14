class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        visited = [[False]*n for _ in range(m)]
        
        def dfs(i,j):
            if board[i][j] != 'O' or visited[i][j]:
                return
            visited[i][j] = True
            moves = [(-1,0),(1,0),(0,1),(0,-1)]
            for di, dj in moves:
                ni, nj = i+di, j+dj
                if not (ni < 0 or ni >= m or nj < 0 or nj >= n):
                    dfs(ni, nj)

        tocheck = []
        for i in range(m):
            if board[i][0] == 'O':
                tocheck.append((i,0))

            if board[i][n-1] == 'O':
                tocheck.append((i, n-1))

        for j in range(n):
            if board[0][j] == 'O':
                tocheck.append((0, j))
            
            if board[m-1][j] == 'O':
                tocheck.append((m-1,j))
                

        for x, y in tocheck:
            dfs(x,y)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'

        return board
