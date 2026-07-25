class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # by floyd warshal algo, multi source shortest path algo
        mat = [[float("inf")]*n for _ in range(n)]
        for i in range(n):
            mat[i][i] = 0

        for u, v, w in edges:
            mat[u][v] = w
            mat[v][u] = w

        for via in range(n):
            for u in range(n):
                for v in range(n):
                    mat[u][v] = min(
                        mat[u][v],
                        mat[u][via] + mat[via][v]
                    )
                    
        numCities = float("inf")
        res = -1
        for i in range(n):
            reachable = len([mat[i][j] for j in range(n) if i != j and mat[i][j] <= threshold])
            print(i, reachable)
            if reachable <= numCities:
                res = i
                numCities = reachable

        return res