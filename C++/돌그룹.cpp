#include<iostream>
#include<algorithm>
#include<queue>
#include<set>


using namespace std;

int A, B, C;

set < pair<pair<int, int>, int>> check;
queue<pair<pair<int, int>, int>> q;


int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> A >> B >> C;
	q.push(make_pair(make_pair(A, B), C));

	//돌을 같은 갯수로 나눌 수 없다.
	if ((A + B + C) % 3 != 0) {
		cout << 0;
		return 0;
	}

	bool pos = false;
	while (!q.empty()) {
		int a = q.front().first.first;
		int b = q.front().first.second;
		int c = q.front().second;

		q.pop();

		if (a == b && b == c && c == a) {

			pos = true;
			break;
		}

		int aa, bb, cc;

		if (a > b) {
			aa = a - b;
			bb = b + b;
			cc = c;
			//같은 수 조합이 나온적 있는지 확인후 큐에 push
			if (check.find(make_pair(make_pair(aa, bb), cc)) == check.end()) {
				check.insert(make_pair(make_pair(aa, bb), cc));
				q.push(make_pair(make_pair(aa, bb), cc));
			}

		}
		if (b > a) {
			aa = a + a;
			bb = b - a;
			cc = c;
			//같은 수 조합이 나온적 있는지 확인후 큐에 push
			if (check.find(make_pair(make_pair(aa, bb), cc)) == check.end()) {
				check.insert(make_pair(make_pair(aa, bb), cc));
				q.push(make_pair(make_pair(aa, bb), cc));
			}
		}
		if (a > c) {
			aa = a - c;
			cc = c + c;
			bb = b;
			//같은 수 조합이 나온적 있는지 확인후 큐에 push
			if (check.find(make_pair(make_pair(aa, bb), cc)) == check.end()) {
				check.insert(make_pair(make_pair(aa, bb), cc));
				q.push(make_pair(make_pair(aa, bb), cc));
			}
		}
		if (c > a) {
			aa = a + a;
			cc = c - a;
			bb = b;
			//같은 수 조합이 나온적 있는지 확인후 큐에 push
			if (check.find(make_pair(make_pair(aa, bb), cc)) == check.end()) {
				check.insert(make_pair(make_pair(aa, bb), cc));
				q.push(make_pair(make_pair(aa, bb), cc));
			}
		}
		if (b > c) {
			aa = a;
			bb = b - c;
			cc = c + c;
			//같은 수 조합이 나온적 있는지 확인후 큐에 push
			if (check.find(make_pair(make_pair(aa, bb), cc)) == check.end()) {
				check.insert(make_pair(make_pair(aa, bb), cc));
				q.push(make_pair(make_pair(aa, bb), cc));
			}
		}
		if (c > b) {
			aa = a;
			bb = b + b;
			cc = c - b;
			//같은 수 조합이 나온적 있는지 확인후 큐에 push
			if (check.find(make_pair(make_pair(aa, bb), cc)) == check.end()) {
				check.insert(make_pair(make_pair(aa, bb), cc));
				q.push(make_pair(make_pair(aa, bb), cc));
			}
		}



	}

	if (pos)cout << 1;
	else cout << 0;
}