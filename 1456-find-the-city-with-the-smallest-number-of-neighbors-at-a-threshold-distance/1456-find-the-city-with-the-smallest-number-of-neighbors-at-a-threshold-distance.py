class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # by floyd warshal algo, multi source shortest path algo
        # mat = [[float("inf")]*n for _ in range(n)]
        # for i in range(n):
        #     mat[i][i] = 0

        # for u, v, w in edges:
        #     mat[u][v] = w
        #     mat[v][u] = w

        # for via in range(n):
        #     for u in range(n):
        #         for v in range(n):
        #             mat[u][v] = min(
        #                 mat[u][v],
        #                 mat[u][via] + mat[via][v]
        #             )

        # by dijkstra
        adj = defaultdict(list)
        for u, v, t in edges:
            adj[u].append((v,t))
            adj[v].append((u,t))

        mat = [[float("inf")]*n for _ in range(n)]
                    
        for i in range(n):
            pq = []
            dist = mat[i]
            dist[i] = 0
            heappush(pq, (0, i))

            while pq:
                dis, node = heappop(pq)

                if dis > dist[node]:
                    continue
                
                for adjNode, edgeWt in adj[node]:
                    if dist[adjNode] > dis + edgeWt:
                        dist[adjNode] = dis + edgeWt
                        heappush(pq, (dist[adjNode], adjNode))

        numCities = float("inf")
        res = -1
        for i in range(n):
            reachable = len([mat[i][j] for j in range(n) if i != j and mat[i][j] <= threshold])
            if reachable <= numCities:
                res = i
                numCities = reachable

        return res