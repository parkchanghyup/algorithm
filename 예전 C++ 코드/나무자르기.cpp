#include<iostream>
#include<algorithm>
typedef long long ll;
using namespace std;

ll N, M;
int arr[1000000];

int main() {
	int max_num = -1;
	cin >> N >> M;
	for (int i = 0; i < N; i++){
		cin >> arr[i];
		max_num = max(max_num, arr[i]);
	}

	//hi는 max_num 으로 시작.
	int lo = 0, hi = max_num;
	// 이분 탐색 시작
	while (lo + 1 < hi) {
		int mid = (lo + hi) / 2;
		// 각 나무에 대해 mid가 절단기 설정 높이일 때 계산해 길이 합 구하기
		long long sum = 0;
		for (int i = 0; i < N; i++)
			if (arr[i] > mid) sum += arr[i] - mid;
		// mid로 M 이상의 길이를 가져갈 수 있음

		
		if (sum >= M) lo = mid;
		// mid로 M 이상의 길이를 가져갈 수 없음
		else hi = mid;
	}
	cout << lo;
	

}