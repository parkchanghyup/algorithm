#include<iostream>


using namespace std;

int n;
int map[21][21];
int visited[21][21];
int visit[100];
int dx[] = { 0,1,-1,-1,1 };
int dy[] = { 0,1,1,-1,-1 };
pair<int, int> p;

void reset2();
void reset();
int dap;


void dfs(int y, int x,int cnt,int arrow,int result) {
	
	if (cnt > 3 || visited[y][x]) {
		reset2();
		return;
	}

	if (visited[p.first][p.second] == 1) {
		dap = result;
		return;
	}

	for (int i = 1; i < 5; i++) {
		int nx = x + dx[i];
		int ny = y + dy[i];

		if (arrow == 1) {    
			if (i == 3) continue;
		}
		else if (arrow == 2) {
			if (i == 4) continue;

		}
		else if (arrow == 3) {
			if (i == 1) continue;
		}
		else if (arrow == 4) {
			if (i == 2) continue;
		} //반대방향 못가게 ..
		 

		if (!visited[ny][nx] && nx > 0 && nx < n && ny>0 && ny < n) {

			visited[nx][ny] = 1;

			if (visit[map[ny][nx]]) {
				reset2();
				return;
			}
			visit[map[ny][nx]] = 1;
			if(i!=arrow)
			dfs(ny, nx, cnt+1, i,result+1);			
			else
				dfs(ny, nx, cnt , i, result + 1);
		}
	}

}

void reset2() {
	for (int i = 0; i < 100; i++) {
		visit[i] = 0;
	}
}

void reset() {
	for (int j = 0; j < n; j++) {
		for (int k = 0; k < n; k++) {
			visited[j][k] = 0;
		}
		
	}
	
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> n;
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				int num;
				cin >> num;
				map[j][k] = num;
			}
		}
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < n; k++) {
				dfs(j, k, 0, 0,0);
				p= make_pair(j, k);
				reset();
			}
		}
		if (dap == 0) cout << -1;
		else 
		cout << dap+1;
	}
}