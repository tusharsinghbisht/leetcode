class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    graph[i+1].append(j+1)

        visited = [False]*n
        def explore(i):
            if visited[i-1]:
                return 0

            visited[i-1] = True
            for j in graph[i]:
                explore(j)

            return 1
        res = 0
        for item in graph:
            res += explore(item)

        return res
