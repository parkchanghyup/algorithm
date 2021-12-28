#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;


int main() {
	int N;
	cin >> N;
	int dp[1003][3];


	int arr[1005][3];
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 3; j++) {
			cin >> arr[i][j];
		}
	}
	dp[0][0] = arr[0][0];   //첫번째 집을 R로 색칠
	dp[0][1] = arr[0][1];   //첫번째 집을 G로 색칠
	dp[0][2] = arr[0][2];   //첫번째 집을 B로 색칠

	for (int i = 1; i < N; i++) {
		dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0];   //i번째 집을 R로 색칠 
		dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1];   //i번째 집을 G로 색칠 
		dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2];   //i번째 집을 B로 색칠 
	}
	cout << min(min(dp[N - 1][0], dp[N - 1][1]), dp[N - 1][2]);


}