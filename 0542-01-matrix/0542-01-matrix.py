
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        queue = deque()       
        ans = [[-1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i,j))

        moves = [(0,1),(0,-1), (1,0), (-1,0)]
        while queue:
            i, j = queue.popleft()
            for di, dj in moves:
                ni, nj = i+di, j+dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n:
                    if ans[ni][nj] == -1:
                        ans[ni][nj] = ans[i][j]+1
                        queue.append((ni, nj))

        return ans
