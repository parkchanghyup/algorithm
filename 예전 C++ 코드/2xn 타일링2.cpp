#include<iostream>

using namespace std;

long long arr[1001];


long long func(int n) {
	if (n == 1) return 1;
	if (n == 2)return 3;
	if (arr[n] != 0) return arr[n];
	arr[n] = (2 * func(n - 2) + func(n - 1)) % 10007;
	return arr[n];
}

int main() {
	int n;
	cin >> n;
	cout << func(n);

}