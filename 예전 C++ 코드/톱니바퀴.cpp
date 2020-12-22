#include<iostream>
#include<vector>

using namespace std;
vector<int> v[4];
// 방향에따라 회전시키는 함수
void turn(int idx, int dir) {
	if (dir == 1) {
		int tmp = v[idx][7];
		for (int i = 7; i > 0; i--) {
			v[idx][i] = v[idx][i - 1];
		}
		v[idx][0] = tmp;
	}

	else {
		int tmp = v[idx][0];
		for (int i = 0; i < 7; i++) {
			v[idx][i] = v[idx][i + 1];
		}
		v[idx][7] = tmp;
	}
}

//오른쪽 톱니바퀴를 확인하는 함수

void right(int idx, int dir) {
	if (idx > 3) return;

	//맨 오른쪽 톱니바퀴
	if (idx == 3) {
		if (v[idx][6] != v[idx - 1][2])
			turn(idx, dir);
	}
	else {
		if (v[idx][6] != v[idx - 1][2]) {
			right(idx + 1, dir * (-1));
			turn(idx, dir);

		}


	}
	return;
}
//왼쪽 톱니바퀴를 확인하는 함수

void left(int idx, int dir) {
	if (idx < 0) return;

	//맨 왼쪽 톱니바퀴
	if (idx == 0) {
		if (v[idx][2] != v[idx + 1][6]) {
			turn(idx, dir);
		}
	}
	else {
		if (v[idx][2] != v[idx + 1][6])
		{
			left(idx - 1, dir * (-1));
			turn(idx, dir);

		}


	}
}
int main() {


	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 8; j++) {
			int num;
			scanf("%1d", &num);
			v[i].push_back(num);
		}
	}

	int k;
	scanf("%d", &k);
	//톱니바퀴를 회전시킨당.
	for (int i = 0; i < k; i++) {
		int a, b;
		scanf("%d%d", &a, &b);

		right(a, (-1) * b);
		left(a - 2, (-1) * b);
		turn(a - 1, b);


	}

	int score = 0;
	if (v[0][0])score += 1;
	if (v[1][0])score += 2;
	if (v[2][0])score += 4;
	if (v[3][0])score += 8;
	printf("%d", score);
}