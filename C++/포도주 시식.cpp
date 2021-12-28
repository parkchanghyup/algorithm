#include<iostream>
#include<algorithm>
using namespace std;


int dp[10001];
int N;
int arr[10001];

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> N;


	for (int i = 1; i <= N; i++) {
		cin >> arr[i];
	}
	dp[1] = arr[1];
	dp[2] = arr[1] + arr[2];
	for (int i = 3; i <= N; i++) {
		dp[i] = max(dp[i-3]+arr[i]+arr[i-1], max(dp[i - 2] + arr[i],dp[i-1]));
		
	}
	cout << dp[N];


}