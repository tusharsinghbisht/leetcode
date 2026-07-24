class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst,
                          int k) {
        vector<vector<pair<int, int>>> adj(n); // < to, cost > [] from index i

        for (auto it : flights) {
            adj[it[0]].push_back({it[1], it[2]});
        }

        queue<pair<int, pair<int, int>>> queue; // cost, <stops, node>
        vector<int> dist(n, 1e9);
        queue.push({0, {0, src}});
        dist[src] = 0;

        while (!queue.empty()) {
            auto top = queue.front();
            queue.pop();
            int cost = top.first;
            int stops = top.second.first;
            int node = top.second.second;

            if (stops > k)
                continue;

            for (auto it : adj[node]) {
                int adjNode = it.first;
                int edgeWt = it.second;

                if (cost + edgeWt < dist[adjNode] && stops <= k) {
                    dist[adjNode] = cost + edgeWt;
                    queue.push({cost + edgeWt, {stops + 1, adjNode}});
                }
            }
        }

        if (dist[dst] == 1e9)
            return -1;
        return dist[dst];
    }
};