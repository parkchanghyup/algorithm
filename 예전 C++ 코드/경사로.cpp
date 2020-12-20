#include<iostream>

using namespace std;
int N, L;
int map[101][101];
bool check[101][101] = { false, };

//가로 체크 (나보다 큰 곳)
bool garo_up(int y,int x) {
	int num = map[y][x];
	if (x - L +1< 0)return false;

	for (int i = x; i > x - L; i--) {
		if (map[y][i] != num || check[y][i]) return false;
	}
	return true;
}

//가로체크 (나보다  낮은 곳)
bool garo_down(int y,int x) {
	int num = map[y][x];
	if (x + L >= N)return false;

	for (int i = x+1; i <= x + L; i++) {
		if (map[y][i]+1 != num || check[y][i]) return false;
	}
	return true;
}

//세로 체크 (나보다 높은곳)
bool sero_up(int y, int x) {
	int num = map[y][x];
	if (y - L+1 < 0)return false;

	for (int i = y; i > y - L; i--) {
		if (map[i][x] != num || check[i][x]) return false;
	}
	return true;
}

//세로체크 (나보다 낮은곳)
bool sero_down(int y, int x) {
	int num = map[y][x];
	if (y + L >= N)return false;

	for (int i = y + 1; i <= y + L; i++) {
		if (map[i][x] + 1 != num || check[i][x]) return false;
	}
	return true;
}

int main() {
	cin >> N >> L;
	int result = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
		}
	}

	for (int i = 0; i < N; i++) {
		bool pos = true;
		for (int j = 0; j < N; j++) {
			if (j == N - 1) continue;

			if (map[i][j] == map[i][j + 1])continue;
			else if (map[i][j] + 1 == map[i][j + 1]) {
				if (garo_up(i,j)) {
					//경사로 설치여부 확인(중복설치 피하기 위해)
					for (int k = j; k > j - L; k--) {
						check[i][k] = true;
					}
					continue;
				}
				else {
					pos = false;
				}
			}
			else if (map[i][j] - 1 == map[i][j + 1]) {
				if (garo_down(i, j)) {
					//경사로 설치여부 확인(중복설치 피하기 위해)
					for (int k = j + 1; k <= j + L; k++) {
						check[i][k] = true;
					}
					j = j + L - 1;
				}
				else {
					pos = false;
				}
			}
			else {
				pos = false;
				break;
			}
		}

		if (pos) {
			result++;
		}

	}


	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			check[i][j] = false;
		}
	}

	for (int j = 0; j < N; j++) {
		bool pos = true;
		for (int i = 0; i< N; i++) {
			if (i == N - 1) continue;

			if (map[i][j] == map[i+1][j])continue;

			else if (map[i][j] + 1 == map[i+1][j]) {
				//경사로 설치여부 확인(중복설치 피하기 위해)
				if (sero_up(i, j)) {
				
					for (int k = i; k > i - L; k--) {
						check[k][j] = true;
					}
					continue;
				}
				else {
					pos = false;
				}
			}

			else if (map[i][j] -1== map[i+1][j ]) {
				if (sero_down(i, j)) {
					//경사로 설치여부 확인(중복설치 피하기 위해)
					for (int k = i + 1; k <= i + L; k++) {
						check[k][j] = true;
					}
					i = i + L - 1;
				}
				else {
					pos = false;
				}
			}
			else {
				pos = false;
				break;
			}
		}

		if (pos) {
			result++;
		}

	}


	cout << result;
}