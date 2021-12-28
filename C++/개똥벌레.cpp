#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

 int INF = 987654321;



int main(void){

	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int N, H;

	cin >> N >> H;

	vector<int> bottom(N / 2), top(N / 2);

	for (int i = 0; i < N / 2; i++) {
		cin >> bottom[i] >> top[i];
	}


	//오름 차순 정렬( lower_bound,upper_bound사용할려면 정렬되어있어야함)
	sort(bottom.begin(), bottom.end());
	sort(top.begin(), top.end());

	int result = INF;
	int cnt = 1;
	for (int i = 1; i <= H; i++) {

		//해당 높이에 겹치는 석순
		int brk = bottom.size() - (lower_bound(bottom.begin(), bottom.end(), i) - bottom.begin());

		//해당 높이에 겹치는 종유석
		brk += top.size() - (upper_bound(top.begin(), top.end(), H - i) - top.begin());

		if (result == brk)cnt++;

		//최소 파괴 수 갱신
		else if (result > brk) {
			result = brk;
			cnt = 1;
		}		
	}
	
	cout << result << " " << cnt << "\n";
}



