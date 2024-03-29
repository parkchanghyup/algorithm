#include<iostream>
#include <string>
#include <vector>

using namespace std;

	int map[110][110] ;

int solution(int m, int n, vector<vector<int>> puddles) {

	for (int i = 1; i <= m; i++) 
			map[i][1] = 1;	
	for (int j = 1; j <= n; j++) 
		map[1][j] = 1;

	
	for (int i = 0; i < puddles.size(); i++) {
		map[puddles[i][0]][puddles[i][1]] = -1;
	}

	for (int i = 1; i <= m; i++) 
	{
		for (int j = 1; j <= n; j++) 
		{
			if (i == 1 && j == 1) continue;
			if (map[i][j] == -1) map[i][j] = 0;
			else map[i][j] = (map[i - 1][j] + map[i][j - 1]) % 1000000007;
		}
	}

	
	return  map[m][n];
}

int main() {

}