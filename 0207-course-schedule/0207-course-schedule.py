class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ kahn's algorithm - kindof detecting if given graph is DAG; because if DAG all courses can be finished; detecting if DAG by kahn's algo """
        # graph = [[] for _ in range(numCourses)]

        # indegree = [0]*numCourses
        # for u, v in prerequisites:
        #     graph[u].append(v)
        #     indegree[v] += 1

        # queue = deque([])
        # for i, v in enumerate(indegree):
        #     if v == 0:
        #         queue.append(i)
        
        # cnt = 0 # toposort length
        # while queue:
        #     e = queue.popleft()
        #     cnt += 1

        #     for node in graph[e]:
        #         indegree[node] -= 1
        #         if indegree[node] == 0:
        #             queue.append(node)
            
        # if cnt == numCourses: # if toposorted array length equal to total vertices it means its a DAG so return True
        #     return True
        # else: # else return false
        #     return False


        """DFS based approach"""
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            adj[a].append(b)

        visited = [0]*numCourses
        pathVisited = [0]*numCourses

        stack = []

        def dfs(i):
            visited[i] = 1
            pathVisited[i] = 1

            for node in adj[i]:
                if not visited[node]:
                    if dfs(node):
                        return True
                elif pathVisited[node]:
                    return True

            pathVisited[i] = 0
            return False

        
        for i in range(numCourses):
            if not visited[i]:
                if dfs(i):
                    return False
        return True


        