#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	vector<pair<long long,long long>> p;
	
	int n;
	cin >> n;
	for (int i = 0; i < n; i++ ) {
		int a, b;
		cin >> a>>b;
		p.push_back(make_pair(b,a));
	}
	sort(p.begin(), p.end());//종료시간 부터 오른차순 정렬
	int result=1;// 하나는 무조건 하니까 1부터시작
	int num = p[0].first;
	for (int i = 1; i < n; i++) {
		if (p[i].second >= num) {//회의 진행이 가능한 가장 빨리끝나는 회의를 진행.
			num = p[i].first;
			result++;
		}

	}
	cout << result;
	

}