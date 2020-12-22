#include<iostream>
#include<vector>
using namespace std;



int dx[] = { 1,-1,0,0 };
int dy[] = { 0,0,1,-1 };
int arr[5][5];
vector<vector<int>> ans;

bool check(vector<int> v) {
	int Size = ans.size();
	for(int i = 0; i < Size; i++) {
		if (ans[i] == v)return false;
	}
	return true;
}


void func(int y,int x,vector<int> v) {
	v.push_back(arr[y][x]);
	if (v.size() == 6) {
		if (check(v))
			ans.push_back(v);
		return;
	}
	for (int i = 0; i < 4; i++) {
		int next_y = y + dy[i];
		int next_x = x + dx[i];
		if (next_x >= 0 && next_x < 5 && next_y >= 0 && next_y < 5) {
			func(next_y, next_x, v);
		}
	}

}

int main() {
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			cin >> arr[i][j];
		}
	}
	vector<int> a;
	
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 5; j++) {
			func(i, j, a);
		}
	}
	cout << ans.size();
}