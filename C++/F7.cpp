#include<iostream>
#include<algorithm>
using namespace std;

int arr[300001];



bool compare(int a, int b) {
	return a > b;
}

int main() {
	
	int N;

	int score = 0;

	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}


	//내림 차순 정렬
	sort(arr, arr + N, compare);
	
	score = arr[0] + 1;
	int result = 1;

	for (int i = 1; i < N; i++) {
		//1등할 가능성이 있다면 result++
		if (arr[i] + N >= score) result++;

		//비교할 점수를 계속 갱신
		score = max(score, arr[i] + i + 1);
	}
	cout << result;
}