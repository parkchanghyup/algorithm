#include<iostream>
#include<algorithm>
#include<math.h>
#include<string>
using namespace std;


int func(int n) {
	if (n / 10 == 0)return 1;
	else if (n / 100 == 0)return 2;
	else if (n / 1000 == 0)return 3;
	else if (n / 10000 == 0)return 4;
	else if (n / 100000 == 0)return 5;
	else if (n / 1000000 == 0)return 6;
	else if (n / 10000000 == 0)return 7;
	else if (n / 100000000 == 0)return 8;
	else if (n / 1000000000 == 0) return 9;
}


int main() {
	int a, b, c, d;
	long arr[51][6];

	cin >> a >> b >> c >> d;

	int arr_len = max(abs(a), max(abs(b), max(abs(c), abs(d))));

	int y = 0;
	int x = 0;
	int num = 1;

	int dir = 0;// 동쪽
	int cnt = 1;

	int count = (arr_len + arr_len + 1) * (arr_len + arr_len + 1);


	//1 입력
	if (y >= a && y <= c && x >= b && x <= d)
		arr[y -a][x -b] = num;

	num++;

	for (int i = 1; i < count; i) {

		//dir =4 -> 동쪽이므로 dir=0으로 갱신
		if (dir == 4) dir = 0;

		for (int j = 0; j < cnt; j++) {
			if (dir == 0) {
				x++;
			}
			else {
				x--;
			}
			if (y >= a && y <= c && x >= b && x <= d)
				arr[y - a][x - b] = num;
			num++;
			i++;
		}
		//방향전환
		dir++;

		for (int j = 0; j < cnt; j++) {
			if (dir == 1) {
				y--;
			}
			else {
				y++;
			}
			if (y >= a && y <= c && x >= b && x <= d)
				arr[y - a][x - b] = num;
			num++;
			i++;
		}

		//방향전환
		dir++;
		//방향으로 나아가는 횟수 증가
		cnt++;
	}



	long max_num = 0;
	for (int i = 0; i <= abs(c - a); i++) {
		for (int j = -1; j <= abs(d-b); j++) {
			max_num = max(max_num, arr[i][j]);
		}
	}
	int back = func(max_num);

	
	for (int i = 0; i <= abs(c-a); i++) {
		for (int j = 0; j <= abs(d-b); j++) {
			string str = "";
			int c = func(arr[i][j]);
	

			for (int i = 0; i < back - c; i++) {
				str.push_back(' ');
				
			}

			cout << str << arr[i][j] << " ";

		}
		cout << endl;
	}


}