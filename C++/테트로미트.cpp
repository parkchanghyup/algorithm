#include<iostream>
#include<cstring>
#include <algorithm>

using namespace std;
int N, M;
int map[510][510];
int visited[510][510];
int max_sum = 0;
int result = 0;
int dx[] = { 0,0,1,-1 };
int dy[] = { 1,-1,0,0 };

void dfs(int y, int x, int cnt, int sum) {

	if (cnt == 3) { //깊이가 4이면 최대값 비교후 return
		max_sum = max(max_sum, sum);

		return;
	}

	for (int i = 0; i < 4; i++) {  //4방향으로 퍼지게
		int next_y = y + dy[i];
		int next_x = x + dx[i];

		if (next_y >= 0 && next_y < N && next_x >= 0 && next_x < M) {
			if (!visited[next_y][next_x]) {
				visited[next_y][next_x] = 1;
				dfs(next_y, next_x, cnt + 1, sum + map[next_y][next_x]);
				visited[next_y][next_x] = 0;
			}
		}
	}
}

int another(int y, int x) {
	int result = 0;
	if (y > 0 && x > 0 && x < M - 1) { //ㅗ
		result = max(result, map[y][x] + map[y - 1][x] + map[y][x + 1] + map[y][x - 1]);
	}
	if (y > 0 && y < N - 1 && x < M - 1) { //ㅏ
		result = max(result, map[y][x] + map[y - 1][x] + map[y + 1][x] + map[y][x + 1]);
	}
	if (y < N - 1 && x>0 && x < M - 1) { //ㅜ
		result = max(result, map[y][x] + map[y + 1][x] + map[y][x + 1] + map[y][x - 1]);
	}
	if (y > 0 && y < N - 1 && x>0) {//ㅓ
		result = max(result, map[y][x] + map[y - 1][x] + map[y + 1][x] + map[y][x - 1]);
	}

	return result;
}
void reset() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			visited[i][j] = 0;
		}
	}

}
int main() {
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			int a;
			cin >> a;
			map[i][j] = a;
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			visited[i][j] = 1;
			dfs(i, j, 0, map[i][j]);
			result = max(result, max_sum);
			result = max(result, another(i, j));

			visited[i][j] = 0;
		}
	}
	cout << result;
}