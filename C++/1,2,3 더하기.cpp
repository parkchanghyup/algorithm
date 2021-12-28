#include<iostream>

using namespace std;
int N;

int cnt = 0;

void func(int num) {
	if (num > N)return;

	if (num == N) cnt++;
	
	func(num + 1);
	func(num + 2);
	func(num + 3);
	
}


int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	int a;
	cin >> a;
	for(int i = 0 ;i<a;i++){
	cin >> N;
	func(0);
	cout << cnt<<"\n";
	cnt = 0;
	}
}