#include<iostream>
#include<cmath>

using namespace std;

int N, sum=0;
int arr[16];


bool pos(int idx) {
	for (int i = 0; i < idx; i++) {
		if(arr[i]==arr[idx]||abs(arr[idx]-arr[i])==idx-i) return false;//대각선 검사 함수
	}
	return true;
}


void DFS(int idx) {
	if (idx == N) {
		sum++;
		return;
	}
	for (int i = 0; i < N; i++) {
		arr[idx] = i;
		if (pos(idx) == true) DFS(idx + 1);
	}


}
int main() {
	cin >> N;
	DFS(0);
	cout << sum;
}