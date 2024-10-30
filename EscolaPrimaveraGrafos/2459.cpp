#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Edge {
    int u, v, cost;
    bool is_ferry;
};

bool cmp(const Edge &a, const Edge &b) {
    if (a.cost != b.cost)
        return a.cost < b.cost;
    return a.is_ferry < b.is_ferry;
}

int find(vector<int> &parent, int u) {
    if (u != parent[u])
        parent[u] = find(parent, parent[u]);
    return parent[u];
}

void unite(vector<int> &parent, vector<int> &rank, int u, int v) {
    int root_u = find(parent, u);
    int root_v = find(parent, v);
    if (root_u != root_v) {
        if (rank[root_u] > rank[root_v]) {
            parent[root_v] = root_u;
        } else if (rank[root_u] < rank[root_v]) {
            parent[root_u] = root_v;
        } else {
            parent[root_v] = root_u;
            rank[root_u]++;
        }
    }
}

int main() {
    int N, F, R;
    cin >> N >> F >> R;
    vector<Edge> edges;

    for (int i = 0; i < F; i++) {
        int A, B, C;
        cin >> A >> B >> C;
        edges.push_back({A, B, C, true});
    }
    for (int i = 0; i < R; i++) {
        int I, J, K;
        cin >> I >> J >> K;
        edges.push_back({I, J, K, false});
    }

    sort(edges.begin(), edges.end(), cmp);

    vector<int> parent(N + 1), rank(N + 1, 0);
    for (int i = 1; i <= N; i++) parent[i] = i;

    int total_cost = 0;
    int edges_used = 0;

    for (const auto &edge : edges) {
        if (find(parent, edge.u) != find(parent, edge.v)) {
            unite(parent, rank, edge.u, edge.v);
            total_cost += edge.cost;
            edges_used++;
            if (edges_used == N - 1)
                break;
        }
    }

    cout << total_cost << endl;

    return 0;
}
