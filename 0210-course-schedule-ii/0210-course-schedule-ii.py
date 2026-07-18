class Solution:
    def findOrder(self, V: int, prerequisites: List[List[int]]) -> List[int]:
        """DFS based approach"""
        adj = [[] for _ in range(V)]
        indegree = [0]*V

        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1


        queue = deque([i for i in range(V) if indegree[i] == 0])
        res = []
        while queue:
            e = queue.popleft()
            res.append(e)
            for node in adj[e]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
        
        if len(res) == V:
            return res
        
        return []