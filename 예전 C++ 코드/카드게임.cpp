#include<iostream>
#include<algorithm>
#include <string>
#include <vector>

using namespace std;
vector<int> a;  // L
vector<int> b;   //R
int Size;
int dp[2002][2002];
int func(int L, int R) {
	if (L == Size || R == Size) return dp[L][R]; //한쪽 카드를 다버리면 끝 ~ 
	if (dp[L][R] != 0) return dp[L][R]; 
	
		dp[L][R] = max(func(L + 1, R), func(L + 1, R + 1)); //왼쪽만 버리거나 둘다버리거나
		if (a[L] > b[R]) {
			dp[L][R] = max(dp[L][R], func(L, R + 1) + b[R]);//오른쪽만 버리고 점수휙득.
		}
		return dp[L][R];

}


int solution(vector<int> left, vector<int> right) {
	a = left;	
	b = right;
	Size = a.size();
	int answer = func(0, 0);
	return answer;
}