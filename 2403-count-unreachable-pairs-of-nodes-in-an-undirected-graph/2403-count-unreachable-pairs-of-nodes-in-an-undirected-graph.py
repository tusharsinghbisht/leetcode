from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        # Returns the size of the connected component
        def dfs(node):
            visited[node] = True
            size = 1

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    size += dfs(neighbor)

            return size

        ans = 0
        remaining = n

        # Find each connected component
        for node in range(n):
            if not visited[node]:
                component_size = dfs(node)

                remaining -= component_size
                ans += component_size * remaining

        return ans