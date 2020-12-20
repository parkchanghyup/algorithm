#include<iostream>

using namespace std;


int dp1[45];
int dp2[45];
int func0(int n) {
	if (dp1[n] != -1)return dp1[n];
	if (n == 0)return 1;
	if (n == 1)return 0;
	
	return dp1[n] = func0(n - 1) + func0(n - 2);

}
int func1(int n) {
	if (dp2[n] != -1)return dp2[n];
	if (n == 0)return 0;
	if (n == 1)return 1;

	return dp2[n] = func1(n - 1) + func1(n - 2);

}


int main() {
	int N;
	cin >> N;
	for (int i = 0; i < 45; i++) {
		dp1[i] = -1;
		dp2[i] = -1;
	}
       
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		cout << func0(num) << " " << func1(num) << "\n";
	}

}