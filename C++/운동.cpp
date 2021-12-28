#include<iostream>
#include<algorithm>


using namespace std;


int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int N, m, M, T, R;
	cin >> N >> m >> M >> T >> R;


	int X = m ;
	int result = 1;
	int cnt =0 ;
	while (1) {

		//휴식이필요해
		if (X + T > M) {
			X -= R;
			if (X < m)X = m;
		}
		else {
			X += T;
			cnt++;
		}


		if (X + T > M && X == m) {
			cout << "-1";
			return 0;
		}

		if (cnt == N) break;
		result++;
	}
	cout << result;


}