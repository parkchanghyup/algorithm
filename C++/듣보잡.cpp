#include<iostream>
#include<string>
#include<algorithm>
#include<vector>


using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	int N, M;
	vector<string> str;
	cin >> N >> M;

	for (int i = 0; i < N+M; i++) {
		string a;
		cin >> a;
		str.push_back(a);
		
	}
	sort(str.begin(), str .end());
	str.push_back(" ");
	vector<string> ans;
	for (int i = 0; i < N + M; i++) {
		if (str[i] == str[i + 1]) {
			ans.push_back(str[i]);
			i++;
		}
	}
	cout << ans.size()<<"\n";
	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i] << "\n";
	}




}


