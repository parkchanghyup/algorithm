#include<iostream>
#include<vector>
using namespace std;

int N, M;
vector<int> num;
vector<int> sum;


int main() {
	scanf_s("%d%d", &N, &M);
	num.push_back(0);
	sum.push_back(0);
	
	for (int i = 1; i <= N; i++) {
		int a;
		scanf_s("%d", &a);
		num.push_back(a);
		sum.push_back(sum[i - 1] + num[i-1]);
	}

	for (int i = 0; i < M; i++) {
		int a, b;
		scanf_s("%d%d", &a, &b);
		printf("%d\n", sum[b] - sum[a] + num[b]);
	}



}