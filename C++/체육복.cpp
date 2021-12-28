#include<iostream>

#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
	int answer = n;
	answer = answer - lost.size();
	
	for (int i = 0; i < lost.size(); i++) {
		int num = lost[i];
		for (int j = 0; j < reserve.size(); j++) {
			if (num == reserve[j]) {
				reserve[j] = -1;
				lost[i] = -1;
				answer++;
			}
		}
	}
	for (int i = 0; i < lost.size(); i++) {
		int num = lost[i];
		if (num == -1) {
	
			continue;
		}
		for (int j = 0; j < reserve.size(); j++) {
			if (reserve[j] == -1) continue;
			if (num == reserve[j] - 1||num==reserve[j]+1) {
				lost[i] = -1;
				reserve[j] = -1;
				answer++;
				break;
			}
			
		}
	}
	
	
	return answer;
}

int main() {
	vector<int> a = { 3,4,7,8};
	vector<int> b = { 1,2,3,4,5,7,8};
	int ans = solution(8, a, b);
	cout << ans;
}