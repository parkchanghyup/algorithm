#include<iostream>
#include<algorithm>
using namespace std;



int main() {
	int arr[1001];
	int N, L,num;
	int big = 0;
	cin >> N >> L;
	for (int i = 0; i < 1001; i++) arr[i] = 0;
	for (int i = 0; i < N; i++) {
		
		cin >> num;
		arr[num] = 1;
		big = max(num, big);
	}
	int result = 0;
	for (int i = 0; i <= big; i++) {
		if (arr[i] == 0)continue;

		result++;
		i = i + L - 1;

	}
	cout << result;
}