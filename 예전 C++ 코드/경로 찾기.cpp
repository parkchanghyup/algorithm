#include<iostream>
#include<algorithm>
using namespace std;


int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	int N,map[101][101];
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
		}
	}

	//플로이드 와샬 알고리즘

	for (int k = 0; k < N; k++) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!map[i][j])
					if (map[i][k] && map[k][j])map[i][j] = 1;
			}
		}

	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << map[i][j] << " ";
		}
		cout << endl;
	}
}
