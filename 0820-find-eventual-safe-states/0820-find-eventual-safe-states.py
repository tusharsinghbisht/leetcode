class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        visited = [0]*V
        pathVisited = [0]*V
        check = [0]*V

        def dfs(i):
            visited[i] = 1
            pathVisited[i] = 1

            for node in graph[i]:
                if not visited[node]:
                    if dfs(node):
                        check[i] = 0
                        return True
                if pathVisited[node]:
                    check[i] = 0
                    return True
            
            check[i] = 1
            pathVisited[i] = 0
            return False

        result = []
        for i in range(V):
            if not visited[i]:
                dfs(i)

        for i in range(V):
            if check[i]:
                result.append(i)

        return result