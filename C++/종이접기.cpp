#include<iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> ans;
vector<int> b;
vector <int> func(int n) {
	if (n == 1) return { 0 };




	b = func(n - 1);
	ans = b;
	ans.push_back(0);
	for (int i = b.size() - 1; i >= 0; i--) {
		int num = b[i];
		if (num == 0)
			ans.push_back(1);
		else
			ans.push_back(0);
	}
	return ans;
}


vector<int> solution(int n) {
	vector<int> answer = func(n);
	return answer;
}

int main() {
	vector<int> a = solution(3);
	for (int i = 0; i < a.size(); i++) {
		cout << a[i] << " ";
	}
}