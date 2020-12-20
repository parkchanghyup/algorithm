#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;
typedef pair<int, int> P;

//컴퓨터 갯수 ,의존성 갯수 , 해킹당한 번호 
int n, d, c;
int check[10001];
vector<P> v[10001];
int visited[10001];
void dijkstra(int start) {
	//자기자신
	check[start] = 0;

	priority_queue<P> PQ;
	PQ.push(P(0, start));

	while (!PQ.empty()) {
		int curr = PQ.top().second;
		int dist = -PQ.top().first;
		PQ.pop();

		if (check[curr] < dist)continue;

		
		for (int i = 0; i < v[curr].size(); i++) {
			int next = v[curr][i].first;
			int next_dist = dist + v[curr][i].second;

			if (next_dist < check[next]) {
				check[next] = next_dist;
				PQ.push(P(-next_dist, next));
			}
		}
	}
}






int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(0);

	int T;
	cin >> T;
	for (int j = 0; j < T; j++) {

		cin >> n >> d >> c;

		for (int i = 0; i < d; i++) {
			int a1, a2, a3;
			cin >> a1 >> a2 >> a3;

			//단방향 그래프
			v[a2].push_back(P(a1, a3));
		}

		//배열 초기화 
		for (int i = 0; i <= n; i++) {
			check[i] = 1000000000;
			visited[i] = 0;
		}

		//다익스트라 
		dijkstra(c);

		//감염 컴퓨터 갯수
		int cnt = 0;

		//감염 시간
		int Time = 0;

		for (int i = 1; i <= n; i++) {
			if (check[i] != 1000000000) {
				cnt++;
				Time = max(Time, check[i]);
			}
		}

		cout << cnt << " " << Time << "\n";
		
		//벡터 초기화
		for (int i = 0; i <= n; i++) {

			int Size = v[i].size();
			for (int k = 0; k < Size; k++) {
				v[i].pop_back();
			}
			
		}
			
	}
}