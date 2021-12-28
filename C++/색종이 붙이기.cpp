#include<iostream>
#include<algorithm>
using namespace std;
int arr[10][10];
int num[6] = { 0,5,5,5,5,5 };
int result = 101;

//종이 붙일수있는지 판단하는 함수.
bool possible(int y, int x, int n) {

	for (int i = y; i < y + n; i++) {
		for (int j = x; j < x + n; j++) {
			if (arr[i][j] != 1)return false;
		}
	}
	return true;
}

void Fill(int y, int x, int n, int num) {
	for (int i = y; i < y + n; i++) {
		for (int j = x; j < x + n; j++) {
			arr[i][j] = num;
		}
	}
}

void func(int y, int x, int cnt) {
	{//가로 탐색이 끝났으면 세로탐색 시작
	if (x == 10){
		func(y + 1, 0, cnt);
		return;
	}
	//세로 탐색이 끝났으면 최소값 갱신
	if (y == 10) {
		result = min(result, cnt);
		return;
	}
	//0 이면 확인할 필요 x
	if (arr[y][x] == 0) {
		func(y, x + 1, cnt);
		return;
	}
	//크기가 5까지 잇으므로 5부터 1까지
	for (int i = 5; i > 0; i--) {
		//범위 초과 , 갯수 초과
		if (x + i > 10 || y + i > 10 || num[i] == 0) continue;// 
		//종이를 붙일수있으면 .
		if (possible(y, x, i)) {
			Fill(y, x, i, 0);//붙이고
			num[i]--;//종이 사용
			func(y, x, cnt + 1);//종이 갯수 ++
			num[i]++;//종이 복구
			Fill(y, x, i, 1);//떼고
		}


	}

}



int main() {

	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++) {
			cin >> arr[i][j];
		}
	}
	func(0, 0, 0);
	if (result == 101) cout << -1;
	else cout << result;
}

