#include<iostream>

using namespace std;

int  arr[101][101];

int main() {

	int n;
	cin >> n;

	for (int i = 1; i <= 9; i++)
		arr[1][i] = 1;

	for (int i = 2; i <= n; i++) {
		for (int j = 0; j <= 9; j++) {
			if (j == 0)
				arr[i][j] = arr[i - 1][1]% 1000000000;
			else if (j == 9) 
				arr[i][j] = arr[i - 1][8]%1000000000;
			else 
				arr[i][j] = (arr[i - 1][j - 1] + arr[i - 1][j + 1]) % 1000000000;
			
		}
	}

	int sum = 0;
	for (int i = 0; i < 10; i++) {
		sum = (sum+arr[n][i]) % 1000000000;
	}
	cout << sum % 1000000000;
}
   