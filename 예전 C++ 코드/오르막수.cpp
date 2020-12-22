#include<iostream>


using namespace std;

int main() {
	int arr[1001][10];
	int n;
	cin >> n;

	for (int i = 0; i < 10; i++) {
		arr[1][i] = 1;
	}
	for(int j = 2;j<=n;j++){
		for (int i = 0; i < 10; i++) {
			arr[j][i] = 0;
		}
	}
	
	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < 10; j++) {
			for (int k = 0; k <= j; k++) {
				arr[i][j] = arr[i][j]+arr[i - 1][k];
				arr[i][j] = arr[i][j] % 10007;
			}
		}
	}

	int sum = 0;
	for (int i = 0; i <10 ; i++) {
		sum = sum + arr[n][i];
		sum %= 10007;
	}
	cout << sum;





}