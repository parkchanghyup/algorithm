#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;
	vector<int> a;
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		a.push_back(num);
	}
	sort(a.begin(), a.end());
	cout << a[0] * a[a.size() - 1];
}