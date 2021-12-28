#include <iostream>
using namespace std;
int arr[501][501];
int dp[501][501];
int visited[501][501];
int m, n;
int dy[4] = { 1, 0, -1, 0 };
int dx[4] = { 0, 1, 0, -1 };

int dfs(int y, int x) {

	if (y == n && x == m) {
		// 오른쪽 끝에 도착하면 1 return
		return 1; 
	}
	if (visited[y][x]) //이미 방문한 곳이라면 dp[y][x] reutrn.
		return dp[y][x];

	for (int i = 0; i < 4; i++) {
		int next_y = y + dy[i];
		int next_x = x + dx[i];

		if (next_y > 0 && next_y <= n && next_x > 0 && next_x <= m)
			if (arr[y][x] > arr[next_y][next_x]){
				dp[y][x] += dfs(next_y, next_x);
				visited[y][x] = 1;
			}

	}
	return dp[y][x];
}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> n >> m;
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= m; j++)
			cin >> arr[i][j];


	cout << dfs(1, 1) << '\n';
	return 0;
}

