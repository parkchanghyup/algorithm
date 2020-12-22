#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>

using namespace std;

typedef pair<int, int> P;

vector<P> V[1001];
vector<int> pos[1001];
int N, M;
int check[1001];
int line[1001];


//다익스트라 알고리즘
void dijkstra(int start) {
	check[start] = 0;
	priority_queue<P> pq;
	pq.push(P(0, start));

	while (!pq.empty()) {
		int curr = pq.top().second;
		int dist = -pq.top().first;
		pq.pop();

		if (dist < check[curr])continue;


		for (int i = 0; i < V[curr].size(); i++) {

			int next = V[curr][i].first;
			int next_dist = V[curr][i].second+dist;

			if (next_dist < check[next]) {
				check[next] = next_dist;
				pq.push(P(-next_dist, next));				

				//재 생성할 네트워크를 갱신.
				line[next] = curr;

			}
		}

		cout << endl;
	}


}
int main() {
	vector<P> dap;
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		V[a].push_back(P(b, c));
		V[b].push_back(P(a, c));
	}
	for (int i = 0; i <= N; i++)check[i] = 100000;
	for (int i = 0; i <= N; i++)line[i] = 0;
	dijkstra(1);
	int cnt = 0;
	for (int i = 0; i <= N; i++) {
		if (line[i])cnt++;
	}

	cout << cnt << "\n";
	for (int i = 1; i <= N; i++) {
		if (line[i]) {
			cout << i <<" " <<line[i] << "\n";
		}
	}


}
