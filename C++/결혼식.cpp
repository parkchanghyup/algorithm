#include<iostream>
#include<algorithm>

using namespace std;

const int INF = 501;
int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int arr[INF][INF];
	int n, m;

	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			arr[i][j] = INF;
		}
	}

	for (int i = 0; i < m; i++) {
		int a, b;

		cin >> a >> b;
		arr[a - 1][b - 1] = 1;
		arr[b - 1][a - 1] = 1;
	}

	for (int k = 0; k < n; k++) {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
			}
		}
	}
	int result = 0;
	for (int i = 1; i < n; i++) {
		if (arr[0][i] < 3)result++;
}
	cout << result;
}