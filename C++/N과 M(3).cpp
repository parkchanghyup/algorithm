#include<iostream>
#include<vector>
using namespace std;



int N, M;


void print(vector<int> a) {
	for (int i = 0; i < M; i++) {
		cout << a[i] << " ";
	}
	cout << "\n";

}
void func(vector<int> a) {
	if (a.size() == M) {
		print(a);
		return;
	}

	for (int i = 1; i <= N; i++) {
		a.push_back(i);
		func(a);
		a.pop_back();
	}
	return;
}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> N >> M;
	
	func({});
}