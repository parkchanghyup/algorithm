#include<iostream>
#include<math.h>

using namespace std;
typedef long long ll;

pair<int, int> prince, flower;

int func(ll y, ll x, ll r) {
	int num = 0;
	
	ll dist = (prince.first - x) * (prince.first - x) + (prince.second - y) * (prince.second - y);

	//왕자가 행성내에 속해있을시
	if (dist <= r*r) {
		num++;
	}

	
	ll dist2 = (flower.first - x) * (flower.first - x) + (flower.second - y) * (flower.second - y);

	//꽃이 같은 행성내에 속해있으시
	if (dist2 <= r*r) {
		num++;
	}

	//둘중 하나만 속해있으면 지나야 하는 행성계 하나 추가
	if (num == 1) return 1;

	//나머지는 행성계를 지나지 않아도된다.
	else return 0;
}

int main() {


	int a, b, c, d, M, T;
	cin >> T;

	for (int i = 0; i < T; i++) {

		cin >> a >> b >> c >> d;
		prince = make_pair(a, b);
		flower = make_pair(c, d);

		cin >> M;
		int result = 0;
		for (int i = 0; i < M; i++) {
			ll x, y, r;
			cin >> x >> y >> r;
			result += func(y, x, r);
		}
		cout << result << "\n";
	}
}