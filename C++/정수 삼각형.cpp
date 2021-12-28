#include<iostream>
#include <string>
#include <vector>
#include<algorithm>
using namespace std;


int solution(vector<vector<int>> triangle) {
	int dp[505][505];
	int size = triangle.size();
	vector<int> t;
	
	dp[1][0] = triangle[0][0] + triangle[1][0];
	dp[1][1] = triangle[0][0] + triangle[1][1];
	for (int i = 2; i < size; i++) {
		int Size = triangle[i].size();
		for (int j = 0; j < Size; j++) {
			
			if (j == 0)dp[i][j] = dp[i - 1][j] + triangle[i][j];
			else if( j==Size-1) dp[i][j]=dp[i-1][j-1]+triangle[i][j];
			else
			dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j];
		}
	}



	int answer = 0;
	int Size = triangle[size-1].size();
	for (int i = 0; i < Size; i++){
		answer = max(dp[size-1][i], answer);
	}

	return answer;

}
int main(){
	int n;
	int num;
	cin >> n;

	vector<vector<int>> a;
	for (int i = 0; i < n; i++) {
		vector<int>b;
		for (int j = 0; j <= i; j++) {

			cin >> num;
			b.push_back(num);
			
		}
		a.push_back(b);
   }
	

	int b = solution(a);
	cout << b;
}