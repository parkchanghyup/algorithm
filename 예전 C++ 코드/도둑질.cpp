#include<iostream>
#include <string>
#include <vector>
#include<algorithm>
using namespace std;



long dp[1000000];
long dp2[1000000];

int solution(vector<int> money) {
	
	int Size = money.size();
	for (int i = 0; i < Size; i++){
		dp2[i] = 0;
		dp[i] = 0;
	}

	dp[0] = money[0];
	dp[1] = money[0];

	dp2[1] = money[1];
	for (int j = 2; j < Size-1; j++) {
			dp[j] = max(dp[j - 1], dp[j - 2] + money[j]);
		}
	for(int j = 2; j < Size; j++) {
		dp2[j] = max(dp2[j - 1], dp2[j - 2] + money[j]);
	}
	
	
	int answer =max( dp[Size-2],dp2[Size-1]);
	return answer;
}
int main(){
	int ans = solution({ 1,2,3,4 });
	cout << ans;
}