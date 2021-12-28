#include<iostream>
#include<queue>


using namespace std;

int map[100][100];
int visited[100][100];

int dx[] = { 1,-1,0,0 };
int dy[] = { 0,0,1,-1 };

int cnt = 0;

void BFS() {
	queue <pair<int, int>> q;
	//시작 점을 q에 push
	q.push(make_pair(0, 0));

	//시작점 방문 체크
	visited[0][0] = 1;

	//큐가 빈 상태가 될때까지 반복
	while (!q.empty()) {

		int size = q.size();

		//cnt는 bfs의 깊이를 나타냄.

		cnt++;

		for (int i = 0; i < size; i++) {
			//q의 front부분을 중심으로
			pair<int, int> x = q.front();
			q.pop();
			int a = x.first;
			int b = x.second;
			//4방향을 탐색한다. 
			for (int j = 0; j < 4; j++) {
				int next_x = a + dx[i];
				int next_y = b + dy[i];

				//배열초과 여부 확인
				if (next_x >= 0 && next_x < 100 && next_y >= 0 && next_y < 100) {
					//이동할 수있고 방문 하지 않았을경우 q에 넣는다.
					if (map[next_x][next_y] && !visited[next_x][next_y]) {
						q.push(make_pair(next_x, next_y));
						visited[next_x][next_y] = 1;
					}
				}
			}
		}
	}

}


int main() {
	cout << cnt;
}