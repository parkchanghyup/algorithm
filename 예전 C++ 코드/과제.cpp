#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	vector<pair<int, int>> p;
	int N;
	cin >> N;
	int Size=0;
	for (int i = 0; i < N; i++) {
		int a, b;
		cin >> a >> b;
		p.push_back(make_pair(b, a));
		Size = max(Size, a);
	}
	sort(p.begin(), p.end());
	vector<int> ans;

	
	for (int i = Size; i >= 1; i--) {
		for (int j =N-1; j >=0; j--) {
			
			if (p[j].second >= i) {
				ans.push_back(p[j].first);
				p[j] = make_pair(0, 0);
								break;
			}
		}
	}
	int sum = 0;
	for (int i = 0; i < ans.size(); i++) {
		sum += ans[i];
	}
	cout << sum;
	
}