#include <vector>
#include<algorithm>
using namespace std;

int dp[100001];

int solution(int K, vector<vector<int>> travel) {
	for (int i = 0; i < travel.size(); i++) {
		for (int j = K; j >= 0; j--) {
			dp[j] = -987654321;
			if (j >= travel[i][0])
				dp[j] = max(dp[j], dp[j - travel[i][0]] + travel[i][1]);
			if (j >= travel[i][2])
				dp[j] = max(dp[j], dp[j - travel[i][2]] + travel[i][3]);
		}
	}
	return dp[K];
}