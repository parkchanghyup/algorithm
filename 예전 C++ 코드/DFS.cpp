#include<iostream>
#include<algorithm>


using namespace std;

int visited[100][100];
int map[100][100];

int dx[] = { 1,-1,0,0 };
int dy[] = { 0,0,1,-1 };


//그래프의 컴포넌트 갯수구하기
int dfsAll() {
	int cnt = 0;
	for (int i = 0; i < 100; i++) {
		for (int j = 0; j < 100; j++) {
			if (!visited[i][j]) {
				dfs(i, j);
				cnt++;
			}

		}
	}
	return cnt;
}
void dfs(int x, int y) {
	//이미방문하였다면 return
	if (visited[x][y]) return;

	//방문 체크
	visited[x][y] = 1;

	//상,하,좌,우 4방향 탐색
	for (int i = 0; i < 4; i++) {
		int next_x = x + dx[i];
		int next_y = y + dy[i];

		if (next_x >= 0 && next_x < 100 && next_y >= 0 && next_y < 100) {\
			//탐색가능하다면 재귀호출.
			if (map[next_x][next_y] && !visited[next_x][next_y])
				dfs(next_x, next_y);
		}
	}
}
int main() {
	int result = dfsAll();
	cout << result;
}