#include<iostream>

using namespace std;



int arr[101][101];

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int N,M;
	cin >> N>>M;
	

	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		//a>b
		arr[a][b] = 1;

		//b<a
		arr[b][a] = -1;
	}



	//플루이드
	for (int k = 1; k <= N; k++) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (i == j)continue;


				//대소관계가 정의되지 않았다면 ,
				if (arr[i][j] == 0) {
					arr[i][j] = arr[i][k] + arr[k][j];
					if (arr[i][j] == 2)arr[i][j] = 1;
					else if (arr[i][j] == -2)arr[i][j] = -1;
					else arr[i][j] = 0;
				}
			}
		}
	}

	for (int i = 1; i <= N; i++) {
		int cnt = 0;
		for (int j = 1; j <= N; j++) {
			if (arr[i][j] == 0)cnt++;
		}
		cout << cnt - 1 << "\n";
	}


}