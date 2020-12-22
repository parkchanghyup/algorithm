#include<iostream>
#include<algorithm>
#include<queue>

using namespace std;

int map[101][101], N, num_map[101][101], visited[101][101];
int dx[] = { 1,-1,0,0 };
int dy[] = { 0,0,1,-1 };


void dfs(int y, int x, int num) {//섬에 숫자 붙이는 코드.
	if (visited[y][x]) return;
	visited[y][x] = 1;
	num_map[y][x] = num;
	

	for (int i = 0; i < 4; i++) {
		int next_y = y + dy[i];
		int next_x = x + dx[i];
		if (next_y >= 0 && next_y < N && next_x >= 0 && next_x < N) {
			if (map[next_y][next_x] && !visited[next_y][next_x]) {
				dfs(next_y, next_x, num);
			}
		}
	}

}
int dfsAll() {//섬에 숫자 붙이기 
	int cnt = 1;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (!visited[i][j] && map[i][j]) {
				dfs(i, j, cnt);
				cnt++;
			}
		}
	}
	return cnt;
}
void reset() { //방문 초기화
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			visited[i][j] = 0;
		}
	}
}

int bfs(int num) { //육지확장
	int result = 0;
	queue<pair<int, int>> q;
	//num_map 에서 num인거 다 큐에 push;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (num_map[i][j] == num)q.push(make_pair(i, j));
		}
	}
	while (!q.empty()) 
	{
		int Size = q.size();
		for (int i = 0; i < Size; i++)
		{
			pair<int, int> p = q.front();
			visited[p.first][p.second] = 1;
			q.pop();
			
			for (int j = 0; j < 4; j++)
			{
				int next_y = p.first + dy[j];
				int next_x = p.second + dx[j];
				if (next_y >= 0 && next_y < N && next_x >= 0 && next_x < N) {
					if (!num_map[next_y][next_x] && !visited[next_y][next_x]) {
						q.push(make_pair(next_y, next_x));
						visited[next_y][next_x] = 1;
					}
					else if (num_map[next_y][next_x] &&num_map[next_y][next_x] != num) {
						return result;
					}
				}
			}
		}

		result++;
	}
}
int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
		}
	}
	int num = dfsAll();
	int ans = 1000000;

	for (int i = 1; i < num; i++) {
		reset();
		ans = min(bfs(i), ans);
	
	}
	cout << ans;






}