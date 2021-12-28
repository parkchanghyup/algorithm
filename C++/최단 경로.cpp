#include<iostream>
#include<vector>
#include<queue>

#include<algorithm>

const int INF = 987654321;
using namespace std;
typedef pair<int, int> P;

int V, E, K;
vector<P> v[20005]; // (이어진 정점번호,정점간 거리)
int min_cost[20005];

void dijstra(int start) {
	min_cost[start] = 0;//시작 위치는 거리 0
	priority_queue<P> pq;
	pq.push(P(start, 0));

	while (!pq.empty()) {
		int curr = pq.top().first;
		//짧은 것이 먼저 오도록 음수화
		int dis = -pq.top().second;
		pq.pop();

		// 최단거리가 아닌경우 continue
		if (min_cost[curr] < dis)continue;

		for (int i = 0; i < v[curr].size(); i++) {

			//선택된  노드의 인접노드
			int next = v[curr][i].first;

			//선택된 노드를 인접 노드로 거쳐서 가는 비용
			int nextdis = dis + v[curr][i].second;

			//기존의 최소비용 보다 낮으면 교체
			if (nextdis < min_cost[next]) {
				min_cost[next] = nextdis;
				pq.push(P(next, -nextdis));
			}

		}

	}
	return;

}


int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);


	cin >> V >> E >> K;

	for (int i = 0; i < E; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		v[a].push_back(P(b, c));
	}
	for (int i = 1; i <= V; i++)min_cost[i] = INF;

	dijstra(K);

	for (int i = 1; i <= V; i++) {
		if (min_cost[i] == INF)
			cout << "INF" << "\n";
		else
			cout << min_cost[i] << endl;

	}




}
