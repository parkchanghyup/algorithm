#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

typedef pair<int, int> P;
typedef pair<int, P> PP;

int INF = 150000;
int N;
int map[130][130];
int check[130][130];
int dy[] = { 0,0,1,-1 };
int dx[] = { 1,-1,0,0 };

//다익스트라
void dijkstra(int y, int x) {
	check[y][x] = 0;
	priority_queue<PP> pq;
	pq.push(PP(0, P(y, x)));

	while (!pq.empty()) {
		int curr_x = pq.top().second.second;
		int curr_y = pq.top().second.first;
		int dist = -pq.top().first;
		//종료부
		if (curr_x == N - 1 && curr_y == N - 1)break;
		pq.pop();

		//현재 거리가 최소거리가 아니면 continue
		if (check[curr_y][curr_x] < dist) continue;



		for (int i = 0; i < 4; i++) {
			int next_x = curr_x + dx[i];
			int next_y = curr_y + dy[i];
			//배열 범위 내부에있는지
			if (next_x >= 0 && next_x < N && next_y >= 0 && next_y < N) {
				//다음 정점 까지의 거리
				int next_dist = dist+map[next_y][next_x];
				//거리가 최소값이면 갱신
				if (next_dist < check[next_y][next_x]) {
					check[next_y][next_x] = next_dist;
					pq.push(PP(-next_dist, P(next_y, next_x)));
				}
			}			
		}
	}
	return;
}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int cnt = 1;
	while (1) {
		cin >> N;
		if (N == 0)break;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> map[i][j];
				check[i][j] = INF;
			}
		}

		dijkstra(0, 0);
		cout << "Problem " << cnt << ": " << map[0][0]+check[N - 1][N - 1] << "\n";

		cnt++;
	}

}

