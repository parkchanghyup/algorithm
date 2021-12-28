#include<iostream>
#include<vector>
using namespace std;

int N;
int map[65][65];
vector<char> v;
void func(int n, int y, int x) {
	
	if (n == 1) {
		if(map[y][x])
		v.push_back('1');
		else
			v.push_back('0');
		return;
	}
	bool zero = true, one = true;

	for (int i = y; i < y+n; i++) {
		for (int j = x; j < x+n; j++) {
			if (!map[i][j]) {
				one = false;
			}
			else  {
				zero = false;
			}
		}
	}
	if (one) {
		v.push_back('1');
	}
	else if (zero) {
		v.push_back('0');
	}
	else {
		v.push_back('(');
		func(n / 2, y, x);
		func(n / 2, y, x + n / 2);
		func(n / 2, y + n / 2, x);
		func(n / 2, y+n/2, x+n/2);
		v.push_back(')');
		}
	
	return;

}


int main() {
	
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
		
			scanf("%1d", &map[i][j]);
		}
	}
	
	func(N, 0, 0);


	for (int i = 0; i < v.size(); i++) {
		cout << v[i];
	}
}