class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        cnt = 0
        for f, t, p in flights:
            if t == dst:
                cnt += 1
            adj[f].append((t, p))

        if cnt == 0:
            return -1

        pq = []
        heappush(pq, (0, -1, src))

        while pq:
            nodePrice, stop, node = heappop(pq)

            if stop > k:
                continue
            if node == dst:
                return nodePrice

            
            for adjNode, edgePrice in adj[node]:
                heappush(pq, (nodePrice + edgePrice, stop+1, adjNode))

        return -1

