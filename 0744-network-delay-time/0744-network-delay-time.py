class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # simple dijkstra
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))

        pq = []
        heappush(pq, (0, k))

        dist = { node: float("inf") for node in range(1, n+1) }
        dist[k] = 0

        while pq:
            dis, node = heappop(pq)

            if dis > dist[node]:
                continue

            for adjNode, edgeWt in adj[node]:
                if dist[adjNode] > dis + edgeWt:
                    dist[adjNode] = dis + edgeWt
                    heappush(pq, (dist[adjNode], adjNode))

        
        res = max(dist.values())
        if res == float("inf"):
            return -1
        return res