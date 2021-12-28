#include<iostream>

using namespace std;


int main() {
	int N, K;
	int arr[11];
	cin >> N >> K;

	for (int i = 0; i < N; i++) 	cin >> arr[i];

	int idx=0;
	for (int i = N-1; i >= 0; i--) {
		if (arr[i] <= K) {
			idx = i;
			break;
		}
	}
	int cnt = 0;
	for (int i = idx; i >= 0; i--) {
		cnt =cnt+ K / arr[i];
		K = K % arr[i];
		if (K == 0)break;
	}
	cout << cnt;

}