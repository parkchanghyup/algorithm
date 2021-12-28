#include<iostream>
#include<algorithm>

using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int N, M, map[101][101];
	cin >> N >> M;

	//배열 초기화
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (i == j)map[i][j] = 0;
			else map[i][j] = 1000000000;
		}
	}

	//간선 정보
	for (int j = 0; j < M; j++) {
		int a, b, c;
		cin >> a >> b >> c;
		map[a - 1][b - 1] = min(map[a - 1][b - 1], c);

	}


	

	//플로이드 와샬 알고리즘
	for (int k = 0; k < N; k++) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				map[i][j] = min(map[i][j], map[i][k] + map[k][j]);
			}
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (map[i][j] == 1000000000) map[i][j] = 0;
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << map[i][j] << " ";
		}
		cout << "\n";
	}
	cout << endl;
	   


}