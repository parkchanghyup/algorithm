#include<iostream>

using namespace std;
int main() {
	int N, M;

	scanf_s("%d%d", &N, &M);

	int sum[1025][1025];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int a;
			scanf_s("%d", &a);
			sum[i + 1][j + 1] = sum[i][j + 1] + sum[i + 1][j] - sum[i][j] + a;
		}
	}
	for (int i = 0; i < M; i++) {
		int a, b, c, d;
		scanf_s("%d%d%d%d", &a, &b, &c, &d);
		printf("%d\n", sum[c][d] - sum[c][b - 1] - sum[a - 1][d] + sum[a - 1][b - 1]);
	}
}