#include<iostream>
#include<vector>
using namespace std;

int map[101][101];
vector<int> v;


void func(int y, int x, int d, int g) {
	map[y][x] = 1;

	//0세대
	v.push_back(d);

	//배열 만들기
	for (int i = 0; i < g; i++) {
		int Size = v.size();
		vector<int> ex;

		for (int j = Size - 1; j >= 0; j--) {

			if (v[j] + 1 > 3) ex.push_back(0);
			else
				ex.push_back(v[j] + 1);
		}

		for (int j = 0; j < Size; j++) {
			v.push_back(ex[j]);
		}

	}
	int Size = v.size();
	int yy = y, xx = x;

	//드래곤 커브 그리기
	for (int i = 0; i < Size; i++) {
		if (v[i] == 0) {
			xx++;
		}
		else if (v[i] == 1) {
			yy--;

		}
		else if (v[i] == 2) {
			xx--;
		}

		else if (v[i] == 3) {
			yy++;
		}
		map[yy][xx] = 1;
	}


	for (int i = 0; i < Size; i++)v.pop_back();
}

//사각형 확인 함수
int square() {
	int result = 0;
	for (int i = 0; i < 100; i++) {
		for (int j = 0; j < 100; j++) {
			if (map[i][j] && map[i + 1][j] && map[i][j + 1] && map[i + 1][j + 1])result++;
		}
	}
	return result;
}

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		int x, y, d, g;

		cin >> x >> y >> d >> g;
		func(y, x, d, g);

	}


	cout << square();
}