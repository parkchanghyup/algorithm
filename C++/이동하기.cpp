#include<iostream>
#include<algorithm>
using namespace std;

int N, M;
int map[1001][1001];
int dp[1001][1001];
int visited[1001][1001];
int dy[] = { 1,1,0 };
int dx[] = { 1,0,1 };



int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
		}
	}

	dp[0][0] = map[0][0];
	for (int i = 1; i < N; i++) {
		dp[i][0] = dp[i - 1][0] + map[i][0];
	}
	for (int j = 1; j < M; j++) {
		dp[0][j] = dp[0][j-1] + map[0][j];
	}
	for (int i = 1; i < N; i++) {
		for (int j = 1; j < M; j++) {
			dp[i][j] = max(dp[i - 1][j], max(dp[i][j - 1], dp[i - 1][j - 1])) + map[i][j];
		}
	}
	cout << dp[N - 1][M - 1];
}