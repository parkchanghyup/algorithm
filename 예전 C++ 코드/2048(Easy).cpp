#include<iostream>
#include<algorithm>
using namespace std;



int N;
int arr[21][21];
int new_map[21][21];
int map[21][21];
int result = 0;
void left() {//왼쪽으로 미는 함수

	for (int i = 0; i < N; i++) {
		int num = 0;
		int idx = 0;
		for (int j = 0; j < N; j++) {
			if (map[i][j] == 0)continue;
			else {
				if (num == 0)num = map[i][j];
				else {
					if (num == map[i][j]) {
						new_map[i][idx++] = num * 2;
						num = 0;
					}
					else {
						new_map[i][idx++] = num;
						num = map[i][j];
					}
				}
			}
		}
		if (num != 0) new_map[i][idx] = num;
	}
	for (int i = 0; i < N; i++) {// new_map 을 ans로 넣어주고 new map은 0으로 초기화
		for (int j = 0; j < N; j++) {
			map[i][j] = new_map[i][j];
			new_map[i][j] = 0;
		}
	}

}
void right() {//오른쪽으로 미는 함수

	for (int i = 0; i < N; i++) {
		int num = 0;
		int idx = N - 1;
		for (int j = N - 1; j >= 0; j--) {
			if (map[i][j] == 0)continue;
			else {
				if (num == 0)num = map[i][j];
				else {
					if (num == map[i][j]) {
						new_map[i][idx--] = num * 2;
						num = 0;
					}
					else {
						new_map[i][idx--] = num;
						num = map[i][j];
					}
				}
			}
		}
		if (num != 0) new_map[i][idx] = num;
	}
	for (int i = 0; i < N; i++) {// new_map 을 ans로 넣어주고 new map은 0으로 초기화
		for (int j = 0; j < N; j++) {
			map[i][j] = new_map[i][j];
			new_map[i][j] = 0;
		}
	}
}
void up() {//위로 올리는 함수

	for (int j = 0; j < N; j++) {
		int num = 0;
		int idx = 0;
		for (int i = 0; i < N; i++) {
			if (map[i][j] == 0)continue;
			else {
				if (num == 0)num = map[i][j];
				else {
					if (num == map[i][j]) {
						new_map[idx++][j] = num * 2;
						num = 0;
					}
					else {
						new_map[idx++][j] = num;
						num = map[i][j];
					}
				}
			}
		}
		if (num != 0) new_map[idx++][j] = num;
	}
	for (int i = 0; i < N; i++) {// new_map 을 ans로 넣어주고 new map은 0으로 초기화
		for (int j = 0; j < N; j++) {
			map[i][j] = new_map[i][j];
			new_map[i][j] = 0;
		}
	}
}
void down() {//아래로 내리는 함수

	for (int j = 0; j < N; j++) {
		int num = 0;
		int idx = N - 1;
		for (int i = N - 1; i >= 0; i--) {
			if (map[i][j] == 0)continue;
			else {
				if (num == 0)num = map[i][j];
				else {
					if (num == map[i][j]) {
						new_map[idx--][j] = num * 2;
						num = 0;
					}
					else {
						new_map[idx--][j] = num;
						num = map[i][j];
					}
				}
			}
		}
		if (num != 0) new_map[idx--][j] = num;
	}
	for (int i = 0; i < N; i++) {// new_map 을 ans로 넣어주고 new map은 0으로 초기화
		for (int j = 0; j < N; j++) {
			map[i][j] = new_map[i][j];
			new_map[i][j] = 0;
		}
	}
}
int check() {// 배열에서 최대값
	int num = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			num = max(num, map[i][j]);
		}
	}
	return num;
}

void func(int cnt) {//재귀로 구현
	if (cnt == 6) return;//5번까지만
	result = max(result, check());

	int copyBoard[21][21];

	//현 보드상태 저장해놓고

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			copyBoard[i][j] = map[i][j];

	right();
	func(cnt + 1);
	//보드 복구
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			map[i][j] = copyBoard[i][j];
	left();
	func(cnt + 1);
	//보드 복구
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			map[i][j] = copyBoard[i][j];
	up();
	func(cnt + 1);
	//보드 복구
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			map[i][j] = copyBoard[i][j];
	down();
	func(cnt + 1);
	//보드 복구
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			map[i][j] = copyBoard[i][j];

}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
		}
	}
	func(0);
	cout << result;
}