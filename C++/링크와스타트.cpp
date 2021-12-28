#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;

int N;
int arr[25][25];
int check[25];
int team1 = 0, team2 = 0;
int result = 2000000;
void func(int n, int cnt, int idx) {
	if (n == cnt) {

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (i == j)continue;
				if (check[i] && check[j]) {
					team1 += arr[i][j];
				}
			}
		}
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (i == j)continue;
				if (!check[i] && !check[j]) {
					team2 += arr[i][j];
				}
			}
		}

		result = min(result, abs(team1 - team2));
		team1 = 0, team2 = 0;
		return;
	}


	for (int i = idx; i <= N; i++) {
		if (check[i]) continue;
		else {
			check[i] = 1;
			func(n, cnt + 1, i);
			check[i] = 0;
		}
	}



}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> N;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cin >> arr[i][j];
		}
	}

	for (int i = 0; i <= N; i++)check[i] = 0;

	//팀원수 1 부터 N/2 까지 
	for (int i = 1; i <= N / 2; i++) {
		func(i, 0, 1);
		for (int j = 0; j <= N; j++)check[j] = 0;
	}
	cout << result;

}
