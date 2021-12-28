#include<iostream>


using namespace std;

long long func(int n, int m) {
	long long a=1, b=1;
	int num = m;
	for (int i = 2; i <= n; i++) {
		b *= i;
	}
	for (int i = 0; i < n; i++) {
		a = a * num;
		num--;
	}
	
	return a / b;
}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int T, N, M;

	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N >> M;
		if (N * 2 < M) {
			cout << func(N, M);
		}
		else {
			cout << func(M - N, M);
		}
		cout << '\n';
	}
}