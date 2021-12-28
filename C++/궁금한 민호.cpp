#include<iostream>
#include<algorithm>

using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);


	int N, map[22][22],del[22][22];
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
			del[i][j] = 0;
		}
	}
	//플로이드
	for (int k = 0; k < N; k++) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {

				if (i == j || i == k || j == k)continue;
				//지워도 되는 거
				if (map[i][j] == map[i][k] + map[k][j])del[i][j] = 1;
				//모순일경우 -1출력후 종료.
				else if (map[i][j] > map[i][k] + map[k][j]) {
					cout << -1;
					return 0;
				}
			}
		}
	}

	int result = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (del[i][j] == 1)map[i][j] = 0;			
		}		
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			result += map[i][j];				
		}
	}
	cout << result / 2;

}