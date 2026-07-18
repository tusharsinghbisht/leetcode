class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # kahn's algorithm - kindof detecting if given graph is DAG; because if DAG all courses can be finished
        graph = [[] for _ in range(numCourses)]

        indegree = [0]*numCourses
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque([])
        for i, v in enumerate(indegree):
            if v == 0:
                queue.append(i)
        
        cnt = 0
        while queue:
            e = queue.popleft()
            cnt += 1

            for node in graph[e]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
            
        if cnt == numCourses:
            return True
        else:
            return False
        


        