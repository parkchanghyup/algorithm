#include<iostream>
#include<algorithm>


using namespace std;

int map[401][401];
int N, M;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> N >> M;

	//배열 초기화
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			map[i][j] = 0;
		}
	}

	
	for (int i = 0; i <M; i++) {
			int a, b;
			cin >> a >> b;
			map[a-1][b-1] = -1;
			map[b-1][a-1] = 1;
	}


	//플루이드 알고리즘
	for(int k=0;k<N;k++){
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (i == j)continue;

			if (map[i][j] == 0) {
				if (map[i][k] == 1 && map[k][j] == 1)
				{
					map[i][j] = 1;
				}
				else if (map[i][k] == -1 && map[k][j] == -1)
				{
					map[i][j] = -1;
				}
			}

			
		}
	}
	}

	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		int a, b;
		cin >> a >> b;
		cout << map[a - 1][b - 1]<<"\n";
	}



}