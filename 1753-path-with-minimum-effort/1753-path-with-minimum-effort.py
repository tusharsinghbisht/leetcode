class Solution:
    def minimumEffortPath(self, mat: List[List[int]]) -> int:
        # code here
        row, col = len(mat), len(mat[0])
        pq = []
        heappush(pq, (0, 0, 0))
        
        dist = [[float("inf")]*col for _ in range(row)]
        dist[0][0] = 0
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while pq:
            diff, r, c = heappop(pq)
            
            if r == row - 1 and c == col - 1:
                return diff
            
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    currDiff = max(diff, abs(mat[r][c] - mat[nr][nc]))
                    if currDiff < dist[nr][nc]:
                        heappush(pq, (currDiff, nr, nc))
                        dist[nr][nc] = currDiff
            
 
     