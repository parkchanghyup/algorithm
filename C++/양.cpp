#include<iostream>


using namespace std;

int R, C;
char map[255][255];
int visited[255][255];

int dy[] = { 1,-1,0,0 };
int dx[] = { 0,0,1,-1 };
int sheep = 0, wolf = 0;

pair<int, int> result = make_pair(0, 0);

void dfs(int y, int x) {
	if (visited[y][x] == 1) return;

	visited[y][x] = 1;


	if (map[y][x] == 'v')wolf++;
	else if (map[y][x] == 'o')sheep++;

	for (int i = 0; i < 4; i++) {
		int next_x = x + dx[i];
		int next_y = y + dy[i];

		if (next_x >= 0 && next_x < R && next_y >= 0 && next_y < C) {

			if (map[next_y][next_x] == '#') continue;
			else {
				dfs(next_y, next_x);
			}

		}
	}

}


int main() {
	cin >> C >> R;

	for (int i = 0; i < C; i++) {
		for (int j = 0; j < R; j++) {
			cin >> map[i][j];
			visited[i][j] = 0;
		}
	}
	for (int i = 0; i < C; i++) {
		for (int j = 0; j < R; j++) {
			if (map[i][j] == '#')continue;
			
			if (visited[i][j] == 0) {
				sheep = 0;
				wolf = 0;
				//양,늑대가 울타리내에 있는 숫자를 구함
				dfs(i, j);

				//양이 더많으면 다음날 남아있는 양의 개체수 증가
				if (sheep > wolf) {
					result = make_pair(result.first + sheep, result.second);
				}
				//그외에는 남아있는 늑대의 개체수 증가
				else {
					result = make_pair(result.first, result.second + wolf);
				}

			}
		}
	}

	cout << result.first << " " << result.second;
}