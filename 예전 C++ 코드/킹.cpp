#include<iostream>
using namespace std;

int map[9][9];
int dy[8] = { 1,1,0,-1,-1,-1,0,1 };
int dx[8] = { 0,1,1,1,0,-1,-1,-1 };
int arrow(string str) {
	if (str == "T") {
		return  0;
	}
	else if (str == "RT") {
		return  1;
	}
	else if (str == "R") {
		return  2;
	}
	else if (str == "RB") {
		return  3;
	}
	else if (str == "B") {
		return  4;
	}
	else if (str == "LB") {
		return  5;
	}
	else if (str == "L") {
		return  6;
	}
	else if (str == "LT") {
		return  7;
	}
}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);

	char c;
	int a;
	//킹 위치 
	cin >> c >> a;
	pair<char, int> king = make_pair(c, a);

	//돌 위치
	cin >> c >> a;
	pair<char, int> stone = make_pair(c, a);


	int N;
	cin >> N;

	//이동 입력.
	string str;
	for (int i = 0; i < N; i++) {
		cin >> str;
		int num = arrow(str);
		pair<char, int> P;

		int s1;
		int s2;

		s1 = king.first - 'A';
		s2 = king.second;
		s1 = s1 + dx[num];
		s2 = s2 + dy[num];
		//킹이 체스판을 나가면 움직이지 않는다.
		if (s1 < 0 || s1 >= 8 || s2 < 1 || s2 > 8)continue;

		P = make_pair(king.first + dx[num], king.second + dy[num]);
		//킹 자리에 돌이 있었으면
		if (P == stone) {

			s1 = stone.first - 'A';
			s2 = stone.second;
			s1 = s1 + dx[num];
			s2 = s2 + dy[num];

			//돌이 체스판을 나가면 움직이지않는다.
			if (s1 < 0 || s1 >= 8 || s2 < 1 || s2 > 8)continue;
			else {
				stone = make_pair(stone.first + dx[num], stone.second + dy[num]);
			}
		}
		king = P;

	}
	cout << king.first << king.second << "\n";
	cout << stone.first << stone.second << "\n";


}