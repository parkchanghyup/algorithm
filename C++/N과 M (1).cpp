#include<iostream>
#include<vector>

using namespace std;

int check[9];
int N, M;
vector<int > a;


void print(vector<int> v) {
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << "\n";
}

void func(vector<int> v) {
	if (v.size() == M) {
		print(v);
		return;
	}

	for (int i = 1; i <= N; i++) {
		if (check[i])continue;
		else if (!check[i]) {
			check[i] = 1;
			v.push_back(i);
			func(v);
			v.pop_back();
			check[i] = 0;
		}
	}
	return;

}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> N >> M;
	func({});
}