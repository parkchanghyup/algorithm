#include<iostream>
#include<algorithm>
#include<string>

using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(0);

	string s;

	int arr[26],cnt=0,idx=-1;

	
	cin >> s;
	
	//알파벳 갯수 배열 초기화
	for (int i = 0; i < 26; i++)arr[i] = 0;

	//알파벳 갯수세기
	for (int i = 0; i < s.size(); i++) {
		arr[s[i] - 'A']++;
	}
	
	for (int i = 0; i < 26; i++) {
		//알파벳 갯수가 홀수
		if (arr[i] % 2 == 1) {
			cnt++;
			idx = i;
		}

	}

	//갯수가 홀수개인 알파벳의 수가 2개이상이면 팰린드롬을 만들 수없음
	if (cnt > 1) {
		cout << "I'm Sorry Hansoo";
		return 0;
	}

	string answer = "";
	for (int i = 0; i < 26; i++) {
		for (int j = 0; j < arr[i] / 2; j++) {
			answer.push_back('A' + i);
		}
	}

	if(idx!=-1)
	answer.push_back('A' + idx);

	for (int i = 25; i >= 0; i--) {

		for (int j = 0; j < arr[i] / 2; j++) {
			answer.push_back('A' + i);
		}
	}

	cout << answer;

}