#include<iostream>
#include<algorithm>

using namespace std;
typedef long long ll;

ll INF = 987654321;
ll arr[805][805];
int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	
	int N, M;
	cin >> N >> M;

	//배열 초기화
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++){
			if (i == j)arr[i][j] = 0;
			else arr[i][j] = INF;
		}
	}

	//간선데이터 입력
	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		arr[a][b] = c;
		arr[b][a] = c;
	}

	//플루이드 와샬
	for (int k = 1; k <= N; k++) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (i == j)continue;
				arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
			}
		}
	}




	int a, b;

	cin >> a >> b;
	//a,b중 먼저 들리는 것이 더 가까운 정점을 이용
	ll result = min(arr[1][a] + arr[a][b] + arr[b][N], arr[1][b] + arr[b][a] + arr[a][N]);
	//최단 거리가 존재 하지 않을경우 -1출력
	if (result >= INF)cout << -1;
	else cout << result;


			
}