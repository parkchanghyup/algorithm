#include<iostream>

using namespace std;

int N, M;
int map[305][305];
int map2[305][305];
int visited[305][305];
int dx[] = { 1,-1,0,0 };
int dy[] = { 0,0,1,-1 };

void dfs(int y,int x) { 
	if (visited[y][x]) return;
	visited[y][x] = 1;

	for (int i = 0; i < 4; i++) {
		int next_x = x + dx[i];
		int next_y = y + dy[i];
		if (next_x >= 0 && next_x < M && next_y >= 0 && next_y < N) {
			if (map[next_y][next_x] != 0){
				dfs(next_y, next_x);
			}
		}
	}
}

int check() {  //DFS로 덩어리 갯수 확인 ..
	int cnt = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if(!visited[i][j]&&map[i][j]!=0){
			dfs(i, j);
			cnt++;
			}
			if (cnt > 2)return 2;
		}
	}
	return cnt;
}

void bing() { //
	for(int i = 0 ;i<N;i++){
		for (int j = 0; j < M; j++) {
			int cnt = 0;			//주변에 0의 갯수 확인할 변수임
			if (map[i][j] == 0)continue;  //0이면확인할 필요가없으니까 continue
			else{
			for (int k = 0; k < 4; k++) {//상하좌우 0 찾는거고 
				int y = i + dy[k];
				int x = j + dx[k];
				if (x >= 0 && x < M && y >= 0 && y < N) {
					if (map[y][x] == 0) { //0이면 cnt++
						cnt++;
					}
				}
			}
			map2[i][j] = map[i][j] - cnt;    //map2에  map에서 cnt 를 빼준 값 대입
			if (map2[i][j] < 0) map2[i][j] = 0; // 음수 처리
			}
	}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			map[i][j] = map2[i][j];
		}
	}
}

void reset() {
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)visited[i][j] = 0;
}
int main() {
	
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
		}
	}
	int result = 0;
	while (1) {//여러번 해야되니까 while 문 .

		int cnt = check();


		if (cnt == 0) {
			cout << 0;
			return 0;
		}
		else if (cnt == 2) {
			cout << result;
			return 0;
		}
		bing();


		reset();
		result++;

	}

}