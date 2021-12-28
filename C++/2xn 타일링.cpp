#include<iostream>

using namespace std;

long long arr[1000001];

long long func(int n) {
	if (n == 1)return 1;
	if (n == 2) return 2;
	if (arr[n] != 0)return arr[n];
	arr[n] = (func(n - 1) + func(n - 2)) % 10007;
	return arr[n];
}

int main() {
	int N;
	cin >> N;
	cout << func(N);

}