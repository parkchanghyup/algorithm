#include<iostream>
#include<vector>
using namespace std;

int map[21][21];
int N, M, x, y, K;
int dice[6];
int copy_dice[6];
bool mov = false;
vector<int> m;
void move_R() {
	if (x < M - 1) {
		for (int i = 0; i < 6; i++) {
			copy_dice[i] = dice[i];
		}
		dice[0] = copy_dice[3];
		dice[2] = copy_dice[0];
		dice[3] = copy_dice[5];
		dice[5] = copy_dice[2];
		x++;
		mov = true;
	}

}
void move_L() {
	if (x > 0) {
		for (int i = 0; i < 6; i++) {
			copy_dice[i] = dice[i];
		}
		dice[0] = copy_dice[2];
		dice[2] = copy_dice[5];
		dice[3] = copy_dice[0];	
		dice[5] = copy_dice[3];
		x--;
		mov = true;
	}
}
void move_U() {
	if (y < N - 1) {
		for (int i = 0; i < 6; i++) {
			copy_dice[i] = dice[i];
		}
		dice[0] = copy_dice[1];
		dice[1] = copy_dice[5];
		
		dice[4] = copy_dice[0];
		dice[5] = copy_dice[4];
		y++;
		mov = true;
	}
}
void move_D() {
	if(y>0){
	for (int i = 0; i < 6; i++) {
		copy_dice[i] = dice[i];
	}
	dice[0] = copy_dice[4];
	dice[1] = copy_dice[0];
	dice[4] = copy_dice[5];
	dice[5] = copy_dice[1];
	y--;
	mov = true;
	}
}


int main() {
	cin >> N >> M >> y>> x >> K;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> map[i][j];
		}
	}
	for (int i = 0; i < K; i++) {

		int num;
		cin >> num;
		mov = false;
		if (num == 1) {
			move_R();
		}
		else if (num == 2) {
			move_L();
		}
		else if (num == 4) {
			move_U();
		}
		else if (num == 3) {
			move_D();
		}
		if (mov){
		if (map[y][x] == 0) map[y][x] = dice[0];
		else {
			dice[0] = map[y][x];
			map[y][x] = 0;
		}
		cout << dice[5] << endl;
		}
	}
}