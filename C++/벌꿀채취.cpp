#include<iostream>
#include<algorithm>


using namespace std;

int N, M, C;
int map[11][11];
int ans1 = 0, ans2 = 0;

int arr[5];
bool sel[5];
int max_num = 0;

int square() {
	int sum = 0;
	for (int i = 0; i < M; i++) {
		if (sel[i] == true) {
			sum = sum + arr[i] * arr[i];
		}
	}
	return sum;
}
int Sum() {
	int sum = 0;
	for (int i = 0; i < M; i++) {
		if (sel[i] == true) {
			sum += arr[i];
		}
	}
	return sum;
}

void pick(int y, int x) {
	int idx = 0;
	for (int i = x; i < x + M; i++) {
		arr[idx++] = map[y][i];

	}

}

void DFS(int idx, int cnt) {

	if (cnt > M) return;

	if (cnt > 0) {
		if (Sum() > C) return;



		if (square() > max_num) {
			max_num = square();

		}
	}


	for (int i = idx; i < M; i++) {
		if (sel[i] == true) continue;
		sel[i] = true;
		DFS(i, cnt + 1);
		sel[i] = false;
	}

}

void reset() {
	for (int i = 0; i < 5; i++) {
		sel[i] = false;
		arr[i] = 0;
	}
}

void func() {
	int y = 0;
	int x = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j <= N - M; j++) {
			pick(i, j);
			DFS(0, 0);
			if (max_num > ans1) {
				ans1 = max_num;
				y = i;
				x = j;
			}
		}
	}

	reset();
	max_num = 0;

	for (int i = 0; i < N; i++) {
		if (i == y) continue;
		for (int j = 0; j <= N - M; j++) {



			pick(i, j);
			DFS(0, 0);
			if (max_num > ans2) {
				ans2 = max_num;

			}
		}
	}
	reset();
	max_num = 0;
}

int main() {
	int T;
	cin >> T;
	for (int k = 1; k <= T; k++) {
		cin >> N >> M >> C;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int num;
				cin >> num;
				map[i][j] = num;

			}
		}

		func();
		cout << "#" << k << " " << ans1 + ans2 << "\n";
		ans1 = 0;
		ans2 = 0;

	}

}