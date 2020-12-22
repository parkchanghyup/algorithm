#include<iostream>
using namespace std;

int N;
int arr[2500][2500];
int ans[3];

void func(int n, int y, int x) {
	if (n == 1) {
		ans[arr[y][x] + 1]++;
		return;
	}
	bool a = true, b = true, c = true;
	for (int i = y; i < y + n; i++) {
		for (int j = x; j < x + n; j++) {
			if (arr[i][j] == -1) {
				b = false;
				c = false;
			}
			else if (arr[i][j] == 0 ){
				a = false;
				c = false;
			}
			else if (arr[i][j] == 1) {
				a = false;
				b = false;
			}
		}
	}
	if (a) {
		ans[0]++;
	}
	else if (b)
	{
		ans[1]++;
	}
	else if (c)
	ans[2]++;
	else {
		for (int i = y; i < y + n; i = i + n/3) {//9등분해서 재귀
			for (int j = x; j < x + n; j = j + n / 3) {
				func(n / 3, i, j);
			}
		}
	}
	return;
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> arr[i][j];
		}
	}
	ans[0] = 0;
	ans[1] = 0;
	ans[2] = 0;
	func(N, 0, 0);
	cout << ans[0] <<"\n"<< ans[1]<<"\n" << ans[2];
}