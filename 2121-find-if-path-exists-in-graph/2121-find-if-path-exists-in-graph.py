class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = {}
        for i in range(n):
            graph[i] = []
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False]*n

        def dfs(i):
            visited[i] = True

            for nbr in graph[i]:
                if not visited[nbr]:
                    if nbr == destination:
                        return True
                    elif dfs(nbr):
                        return True
            return False

        return dfs(source)        