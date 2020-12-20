#include<iostream>

using namespace std;


int main() {
	int N,M;
	int arr[100001];
	scanf_s("%d", &N);
	
	for (int i = 0; i < N; i++) {
		int a;
		scanf_s("%d", &a);
		arr[i + 1] = arr[i] + a;
	}
	scanf_s("%d", &M);

	for (int i = 0; i < M; i++) {
		int a, b;
		scanf_s("%d%d", &a, &b);
		printf("%d\n", arr[b ] - arr[a-1]);
	}


}