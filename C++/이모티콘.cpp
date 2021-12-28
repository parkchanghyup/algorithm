
#include<iostream>
#include<algorithm>
using namespace std;

int N;

int arr[2000];

void func(int n, int cnt, int copy) {


	//최솟값 갱신
	if (arr[n] > cnt || arr[n] == 0)
		arr[n] = cnt;
	else
		return;

	//1빼기
	if (n > 1 )
		func(n - 1, cnt + 1, copy);


	//붙여넣기
	if (n + copy < 2000 && copy > 0 )
		func(n + copy, cnt + 1, copy);


	//모두 복사해서 붙여넣기
	if (n + n < 2000 && n > 0 )
		func(n + n, cnt + 2, n);

}



int main() {
	cin >> N;
	arr[1] = 1;
	func(2, 2, 1);
	cout << arr[N];

}
