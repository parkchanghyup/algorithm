#include<iostream>
#include<queue>
#include<algorithm>
#include<vector>

using namespace std;
typedef pair<int, int> P;

int INF = 9867654321;
int N, M, X;
int check[1001][1001];
vector<P> v[1001];

void dijkstra(int start) {
	check[start][start] = 0;
	priority_queue<P> pq;
	pq.push(P(0,start));

	while (!pq.empty()) {
		int curr = pq.top().second;
		int dis = -pq.top().first;
		pq.pop();

		if (check[start][curr] < dis) {
			continue;
		}

		for (int i = 0; i < v[curr].size(); i++) {
			int next = v[curr][i].first;
			int next_dis =dis+ v[curr][i].second;

			if (next_dis < check[start][next]) {
				check[start][next] = next_dis;
				pq.push(P(-next_dis, next));
			}
		}

	}


}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> N >> M >> X;


	//간선 입력
	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		v[a].push_back(P(b, c));
	}

	//배열 초기화
	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <= N; j++) {
			check[i][j] = INF;
		}
	}

	//다익스트라
	for (int i = 1; i <= N; i++) {
		dijkstra(i);
	}

	//결과값
	int result = 0;
	for (int i = 1; i <= N; i++) {
		result = max(result, check[i][X] + check[X][i]);
	}

	cout << result;


}