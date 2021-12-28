#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int N, K;
	int arr[101];
	vector<int> mult;
	cin >> N >> K;
	int result = 0;
	for (int i = 0; i < K; i++) {
		cin >> arr[i];
	}
	mult.push_back(arr[0]);

	for (int i = 1; i < K; i++) {
		
		if (mult.size() == N) {// 플러그가 모두 사용중
			bool pos = false;
			for (int j = 0; j < N; j++) {
				if (arr[i] == mult[j]) {//플러그가 이미 꼽혀있다
					pos = true;
				}
			}
			if (pos == true) continue;
			else {//플러그가 꼽혀있지않다 .
				result++;//플러그를 1회 빼기 떄문에 result++;
				vector<pair<int, int>> p;

				for (int j = 0; j < N; j++) {
					int idx = 100; //idx 최대값
					for (int k = i; k < K; k++) {
						if (mult[j] == arr[k]) {//꼽혀있는 플러그중 언제 사용할 건지 찾아야됨
							idx = k;
							break;
						}
					}
					p.push_back(make_pair(idx, mult[j]));//사용할 일이없으면 idx 는100그대로
				}
				::sort(p.begin(), p.end());
			
				mult[N-1] = arr[i];// 새전기제품 꼽기
				for (int j = 0; j < N-1; j++) {
					mult[j] = p[j].second;  //가장 나중에 사용할 제품뺴고는 안뺴도되니까 고대로 나둔다
				}
			}
		}
		else {//플러그가 모두 사용중이 아니다
			bool pass = false;
			for (int j = 0; j < mult.size(); j++) {
				if (arr[i] == mult[j]) {//이미 꼽혀있으면 pass
					pass = true;
					break;
				}
			}
			if (!pass)mult.push_back(arr[i]);//꼽혀있지않으면 꼽는다.
		}
	}
	cout << result;

}