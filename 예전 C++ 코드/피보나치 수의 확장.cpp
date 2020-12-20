#include<iostream>


using namespace std;


typedef long long ll;


ll dp[1000000];
ll dp_minus[1000000];

ll fibonachi(int n) {
	if (n == 0)return 0;
	if (n == 1)return 1;
	if (n == -1)return 1;

	

	if (n < -1)
	{
		int num = abs(n);
		if (dp_minus[num]!=0)return dp_minus[num];
		else{
		dp_minus[num] = (fibonachi(n +2) - fibonachi(n +1))%1000000000;
		return dp_minus[num];
		}
	}
	else{
		if (dp[n]!=0) return dp[n];
		else dp[n] = (fibonachi(n -2) + fibonachi(n - 1))%1000000000;
		return dp[n];
	}


}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int n;
	cin >> n;
	
		for (int i = 0; i < abs(n); i++ ){
			dp_minus[i] = 0;
			dp[i] = 0;
		}
		ll result = fibonachi(n);
		
	if( result <0){
		cout << -1 << "\n";
		cout << abs(result);
	}
	else if (result > 0) {
		cout << 1 << "\n";
		cout << result;
	}
	else {
		cout << 0 << "\n" << 0;
	}
}

