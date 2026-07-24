class Solution {
public:
    int countPaths(int V, vector<vector<int>>& edges) {
        vector<vector<pair<long, long>>> adj(V); // <node, time>[]
        // creating adjancy list
        for (auto it: edges) {
            adj[it[0]].push_back({ it[1], it[2] });
            adj[it[1]].push_back({ it[0], it[2] });
        }

        long mod = (long)(1e9 + 7);

        // min heap to store < cost, node >
        priority_queue<pair<long, long>, vector<pair<long, long>>, greater<pair<long, long>>> pq;
        vector<long> dist(V, LONG_MAX); // min dist to each node
        vector<long> ways(V, 0); // no of ways a node can be reached
        
        // for starting node dist is 0
        dist[0] = 0;
        // for starting node number of ways is 1 (fixed)
        ways[0] = 1;

        // push (0, 0), i.e (<starting_cost>, <starting_node>)
        pq.push({ 0, 0 });

        // iterate until empty pq
        while (!pq.empty()) {
            long dis = pq.top().first;
            long node = pq.top().second;
            pq.pop();

            if (dis > dist[node]) continue;

            for (auto [adjNode, edgeWt]: adj[node]) {
                // if adjNode hasn't been reached
                if (dist[adjNode] > dis + edgeWt) {
                    dist[adjNode] = dis + edgeWt;
                    pq.push({ dis + edgeWt, adjNode });
                    ways[adjNode] = ways[node];
                }
                // if adjNode has been reached before with same distance, then update the number of ways
                else if (dist[adjNode] == dis + edgeWt) {
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod;
                }
            }
        }

        // return weys in which we can reach last element (i.e index V-1)
        return ways[V-1];
    }
};