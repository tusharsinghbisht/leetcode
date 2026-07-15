class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)+1

        count = [0]*(n+1)

        for u, v in edges:
            count[u] += 1
            count[v] += 1

        for i in range(1, n+1):
            if count[i] == n-1:
                return i

        return -1