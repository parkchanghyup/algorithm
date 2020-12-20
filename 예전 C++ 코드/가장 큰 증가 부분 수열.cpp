#include<iostream>
#include<algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;
	int arr[1001];
	int dp[1001];
	for (int i = 0; i < N; i++)cin >> arr[i];

	for (int i = 0; i < N; i++)dp[i] = 0;

	for (int i = 0; i < N; i++) {
		int num = 0;
		for (int j = i; j >= 0; j--) {
			
			if (arr[i] > arr[j]) {//자기보다 낮은 인덱스에서 낮은 값을 발견 했다 .
				num =max(num, arr[i] + dp[j]); //그중 최대값을 찾는거 .
			}
			
			
		}
		dp[i] = num;
		if (dp[i] == 0)dp[i] = arr[i];// 자기보다 아래 인덱스에서 자기 보다 낮은숫자가 없으면 그냥 자기를 DP 배열에 넣음.
	}
	int result = 0;

	for (int i = 0; i < N; i++) {
		result = max(result, dp[i]);
	}
	cout << result;

}