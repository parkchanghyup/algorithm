#include<iostream>

using namespace std;

int map[55][55];
int robot;
int N, M,r,c,d;
pair<int, int> p;
int result = 0;
bool possible = false;
void spin() { //방향 회전 
	d--;
	if (d < 0) d = 3;
}
void front() {
	
	if (d == 0) {//북
		p = make_pair(-1, 0);
	}
	else if (d == 1)//동
		p = make_pair(0, 1);
	else if (d == 2)//남
		p = make_pair(+1, 0);
	else//서
		p = make_pair(0, -1);
}
void back() {
	if (d == 0) {//북
		p = make_pair(+1, 0);
	}
	else if (d == 1)//동
		p = make_pair(0, -1);
	else if (d == 2)//남
		p = make_pair(-1, 0);
	else//서
		p = make_pair(0, +1);
}

void check() {
	spin();
	front();
	if (map[r + p.first][c + p.second] == 0) {
		possible = true;
	}
}
void func() {

	while (1) {
		if (map[r][c] == 0) {
			map[r][c] = 2;
			
			result++;

			
		}
		for (int i = 0; i < 4; i++) {//
			check();
		}

		if (!possible) {
			back();
			if (map[r + p.first][c + p.second] != 1) {
				r = r + p.first;
				c = c + p.second;
				continue;
			}
			else return;

		}

		spin();
		front();

		if (map[r + p.first][c + p.second] == 0) {
			r = r + p.first;
			c = c + p.second;
		}

		else if(map[r + p.first][c + p.second] != 0)
			continue;
		

		possible = false;
		
	}

}

int main() {
	cin >> N >> M;
	cin >> r>> c >> d;

	for (int i = 0; i < N; i++) 
		for (int j = 0; j <M ; j++) 
			cin >> map[i][j];


	func();
	cout << result;
}

