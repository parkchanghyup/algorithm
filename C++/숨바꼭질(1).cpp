#include<iostream>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;

typedef pair<int, int> P;
int N, M;
int check[20001];
vector<int> v[20001];
int INF = 9876543321;
void dijkstra(int start) {
	check[start] = 0;
	priority_queue<P> pq;
	pq.push(P(0, start)); 
	
	while(!pq.empty()){
		int curr = pq.top().second;
		int dist = -pq.top().first;
		pq.pop();

		if (dist > check[curr])continue;

		for (int i = 0; i < v[curr].size(); i++) {
			int next = v[curr][i];
			int next_dist = dist + 1;
			
			if (next_dist < check[next]) {
				check[next] = next_dist;
				pq.push(P(-next_dist, next));
			}
		}
	}
	return;

}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> N >> M;


	//간선 입력
	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		v[a].push_back(b);
		v[b].push_back(a);
	}

	for (int i = 0; i <= N; i++)check[i] = INF;

	//다익스트라.
	dijkstra(1);

	for (int i = 0; i <= N; i++) {
		if (check[i] >= INF)check[i] = 0;
	}
	int max_num = 0;
	//최대값 구하기
	for (int i = 0; i <= N; i++) {
		max_num = max(max_num, check[i]);
	}

	int result1 = -1, result2 = 0;

	for (int i = 0; i <= N; i++) {
		if (check[i] == max_num) {
			result2++;
			if (result1 == -1) {
				result1 = i;
			}
		}
	}
	cout << result1 << " " << max_num << " " << result2;
}
