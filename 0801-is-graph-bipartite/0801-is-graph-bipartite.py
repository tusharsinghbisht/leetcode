class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # visited = [0]*n
        color = [-1]*n

        def bfs(start):
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
        
                for nbr in graph[node]:
                    if color[nbr] == -1:
                        color[nbr] = 1 - color[node]
                        queue.append(nbr)
                    if color[nbr] == color[node]:
                        return False

            return True

        for i in range(n):
            if color[i] == -1:
                if not bfs(i):
                    return False

        return True