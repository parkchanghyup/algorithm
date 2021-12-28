#include<iostream>
#include<algorithm>

using namespace std;


int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int N, M;
	int arr[505][505];
	cin >> N >> M;

	//배열 초기화
	for (int i = 0; i <= N; i++) {
		for (int j = 0; j <= N; j++) {
			arr[i][j] = 0;
		}
	}

	for (int i = 0; i < M; i++) {
		int a,b;
		cin >> a >> b;
		arr[a][b] = 1;
		arr[b][a] = -1;
	}

	for (int k = 1; k <= N; k++) {
		for (int i = 0; i <= N; i++) {
			for (int j = 0; j <= N; j++) {
				if (arr[i][j]!=0)continue;
				
				if (arr[i][k] + arr[k][j] == 2) {
					arr[i][j] = 1;
				}
				else if (arr[i][k] + arr[k][j] == -2)
					arr[i][j] = -1;

				else
					arr[i][j] = 0;
			}
		}
	}

	int cnt = 0;
	for (int i = 1; i <= N; i++) {
		bool pos = true;
		for (int j= 1; j <= N; j++) {
			if (i == j)continue;
			if (!arr[i][j])pos = false;
		}
		if (pos)cnt++;
	}
	cout << cnt;
}