#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>


using namespace std;

typedef pair<int, int> P;
int INF = 987654321;
int N, M;
vector<P> v[1005];
int check[1005];
void dijkstra(int start) {
	check[start] = 0; //시작 위치는 거리 0
	priority_queue<P> pq;
	pq.push(P(start, 0)); // 시작점 넣어주고 

	while (!pq.empty()) {
		int curr = pq.top().first;
		int dis = -pq.top().second;

		pq.pop();

		//최단거리가 아닌경우 continue
		if (check[curr] < dis)continue;

		for (int i = 0; i < v[curr].size(); i++) {

			//선택된 노드의 인접노드
			int next = v[curr][i].first;
			
			//선택된 노드를 인접 노드로 거쳐서 가는 비용
			int nextdis = dis + v[curr][i].second;			
			if (nextdis < check[next]) {
				check[next] = nextdis;
				pq.push(P(next, -nextdis));
			}
		}
	}
	return;

}


int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);


	cin >> N>>M;

	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		v[a].push_back(P(b, c));
	}
	int s, e;
	cin >> s >> e;
	for (int i = 1; i <= N; i++) check[i] = INF;
	dijkstra(s);

	cout << check[e];

}