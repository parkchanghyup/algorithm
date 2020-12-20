#include<iostream>
#include<algorithm>
using namespace std;


int dp[301];
int arr[301];

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	int N;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> arr[i];
	}
	for (int i = 0; i <= N; i++)dp[i] = 0;

	dp[1] = arr[1];
	dp[2] = arr[1] + arr[2];
	dp[3] = max(dp[1] + arr[3], dp[0]+arr[2] + arr[3]);

	for (int i = 4; i <= N; i++) {
		dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i]);
	}
	cout << dp[N];
}