#include<iostream>

using namespace std;

typedef long long ll;

int main() {
	ll N;
	cin >> N;


	int result = 0;
	int num = 1;
	while (N >= 0) {
		N = N - num;
		num++;
		result++;
	}

	cout << result -1;


}