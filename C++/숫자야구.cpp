#include<iostream>

#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> baseball) {
	int size = baseball.size();
	int arr[1005];

	for (int i = 111; i < 1000; i++) {
		arr[i] = 1;
	}
	for (int i = 0; i < size; i++) {
		int num = baseball[i][0];
		int a = num / 100;  //100의 자리
		int b = num % 100 / 10; //10의 자리
		int c = num % 10; // 1의자리

		int strike = baseball[i][1];
		int ball = baseball[i][2];

	
		for (int j = 111; j < 1000; j++) {
			int str = 0;
			int bal = 0;

			int aa = j / 100;//100의자리
			int bb = j % 100 / 10; //10의 자리
			int cc = j % 10; //  1의 자리
			if (aa == 0 || bb == 0 || cc == 0|| aa == bb || aa == cc || bb == cc) {
				arr[j] = 0;
				continue;
		
			}

			if (aa == a)str++;
			if (bb == b)str++;
			if (cc == c)str++;
			if (aa == b || aa == c) bal++;
			if (bb == a || bb == c) bal++;
			if (cc == b || cc == a) bal++;
			if (strike != str || ball != bal) {
				arr[j] = 0;
			}
		}
	
	}

	int answer = 0;
	for (int i = 111; i < 1000; i++) {
		if (arr[i] == 1) answer++;
	}
	
	return answer;
}

int main() {
	vector<vector<int>> a = { {123,1,1},{356,1,0},{327,2,0},{489,0,1 } };

	int num = solution(a);

	cout << num;
}