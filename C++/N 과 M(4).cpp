#include<iostream>
#include<vector>


using namespace std;



int N, M;

void print(vector<int> v) {
	for (int i = 0; i < v.size(); i++)
		cout << v[i] << " ";

	cout << "\n";

}

void func(int idx,vector<int> v) {
	
	//Á¾·áºÎ.
	if (v.size() == M) {
		print(v);
		return;
	}

	for (int i = idx; i <= N; i++) {
		v.push_back(i);
		func(i, v);
		v.pop_back();

	}
	return;


}


int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	cin >> N >> M;

	func(1, {});
	return 0;
}