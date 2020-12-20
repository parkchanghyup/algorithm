#include<iostream>

using namespace std;

bool arr[10000];
int n, num[4] = { 1,5,10,50 };
int result = 0;
void func(int cnt,int number,int idx) {
	

	//cnt=n 일때 이미 숫자를 만든적이있으면 return 
	//없으면 result++
	if (cnt == n) {
		if (arr[number])return;
		arr[number] = 1;
		result++;
		return;
	}

	
	for (int i = idx; i < 4; i++) {
		func(cnt + 1, number + num[i],i);
	}


}

int main() {

	cin.tie(NULL);
	ios::sync_with_stdio(0);


	cin >> n;
	func(0, 0,0);
	cout << result;

}