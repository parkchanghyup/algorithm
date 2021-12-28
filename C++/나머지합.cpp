#include<iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false); cin.tie(0);
	int N, M;
	long long sum = 0;
	long long mod[1001] = { 0, };
	long long result = 0;
	cin >> N >> M;

	

	for (int i = 0; i < N; i++) {
		
		int a;
		cin >> a;
		sum = (sum + a) % M;
		if (!sum)result++;
		mod[sum]++;
	}

	for (int i = 0; i <M; i++) {
		result = result+mod[i] * (mod[i] - 1) / 2;
	}
	cout << result;

}