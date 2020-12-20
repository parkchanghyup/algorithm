#include<iostream>

#include <string>
#include <vector>

using namespace std;

long long arr[100];
long long func(int n) {
	if (n == 1) {
		return 4;
	}
	if (n == 2)
		return 6;

	if (arr[n] != 0)return arr[n];

	arr[n] = func(n - 1) + func(n - 2);
	return arr[n];
}


long long solution(int N) {
	long long answer = 0;
	

	answer = func(N);
	return answer;
}

int main() {
	cout << solution(5);
}