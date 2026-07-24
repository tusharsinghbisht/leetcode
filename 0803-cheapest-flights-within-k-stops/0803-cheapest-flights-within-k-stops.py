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

        queue = deque()
        price = [float("inf")]*n
        price[src] = 0

        queue.append((0, 0, src))

        while queue:
            cost, stops, node = queue.popleft()

            if stops > k:
                continue

            for adjNode, edgePrice in adj[node]:
                if price[adjNode] > cost + edgePrice:
                    price[adjNode] = cost + edgePrice
                    queue.append((cost+edgePrice, stops+1, adjNode))
        
        if price[dst] != float("inf"):
            return price[dst]
        return -1       

