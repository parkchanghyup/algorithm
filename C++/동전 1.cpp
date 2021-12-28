#include<iostream>
#include<algorithm>
using namespace std;
int coin[101];
int dp[10001];

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int n, k;
	cin >> n >> k;

	//동전 입력
	for (int i = 0; i < n; i++) {
		cin >> coin[i];
	}

	//오름차순 정렬
	sort(coin, coin + n);
	
	//dp 초기화
	dp[0] = 1;
	for (int i = 1; i <= k; i++) {
		dp[i] = 0;
	}

	for (int i = 1; i <= k; i++) {
		//첫번째 코인 이용
		if (i % coin[0] == 0)dp[i] = 1;
	}
	for (int j = 1; j < n; j++) {
		//나머지 코인 이용 
		for (int i = coin[j]; i <= k; i++) {
			dp[i] = dp[i - coin[j]] + dp[i];
		}
	}
	cout << dp[k];
}