#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>



using namespace std;

typedef pair<int, int> P;
typedef pair<int,P> PP; //(dist,y,x)

int N, M;
int map[105][105];
int dx[] = { 1,-1,0,0 };
int dy[] = { 0,0,1,-1 };
int check[105][105];


//다익스트라
void dijkstra(int y, int x) {
	check[y][x] = 0;
	priority_queue<PP> pq;
	pq.push(PP(0, P(y, x)));   //(dist,y,x)
	while (!pq.empty()) {
		int curr_y = pq.top().second.first;
		int curr_x= pq.top().second.second;
		//종류 부
		if (curr_y == N - 1 && curr_x == M - 1)break;
		int dis = -pq.top().first;
		pq.pop();

		//거리가 최소값이아니면 continue
		if (check[curr_y][curr_x] < dis)continue;

		for (int i = 0; i < 4; i++) {
			int next_x = curr_x + dx[i];
			int next_y = curr_y + dy[i];
			if (next_x >= 0 && next_x < M && next_y >= 0 && next_y < N) {
				int next_dis = dis + map[next_y][next_x];
				if (next_dis < check[next_y][next_x]) {
					check[next_y][next_x] = next_dis;
					pq.push(PP(-next_dis,P (next_y, next_x)));
				}
			}
						
		}
	}

	return;

}


int main() {

	scanf("%d%d", &M, &N);

	//배열 입력
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			scanf("%1d", &map[i][j]);
			//최대값으로 초기화.
			check[i][j] = 10001;
		}
	}
	dijkstra(0, 0);

	printf("%d", check[N-1][M-1]);
		
}
