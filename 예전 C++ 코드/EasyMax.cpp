#include<iostream>
#include<math.h>
using namespace std;

int main() {
	int n,m;
	int num[1001];
	int arr[1001];

	scanf_s("%d%d", &n,&m);
	
	for (int i = 0; i < n; i++) {
		scanf_s("%d", &num[i]);
		arr[i] = arr[i-1]+abs(num[i] - num[i - 1]);
		}
	for (int i = 0; i < m; i++) {
		int a, b;
		scanf_s("%d%d", &a, &b);
		printf("%d\n", arr[b-1] - arr[a - 1]);
	}

	

}