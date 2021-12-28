#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int N, M;
vector<vector<int>> ans;
int chk[9];
void print(vector<int> v) {
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << "\n";
}

bool check(vector<int> v) {
	sort(v.begin(), v.end());
	for (int i = 0; i < ans.size(); i++) {
		if (ans[i] == v)return false;
	}
	return true;
}

void func(vector<int> a) {

	if (a.size() == M) {
		if (check(a)) {			
			ans.push_back(a);
		}
		return;
	}

	for (int i = 1; i <= N; i++) {
		if (chk[i])continue;

		else {
			chk[i] = 1;
			a.push_back(i);
			func(a);
			a.pop_back();
			chk[i] = 0;
		}
	}

}


int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> N >> M;

	for (int i = 0; i <= M; i++)chk[i] = 0;
	func({});

	for (int i = 0; i < ans.size(); i++) {
		for (int j = 0; j < M; j++) {
			cout << ans[i][j] << " ";
		}
		cout << "\n";
	}



}