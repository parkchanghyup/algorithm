#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;


long long n;
long long arr[100001];



int main() {
	for (int  i = 1; i <= 100000; i++)
		arr[i] = 100001;

	cin >> n;


	for (int i = 1; i <= n; i++) {

		for (long long j = i*i; j <= n; j++) {
			arr[j] = min(arr[j], arr[j - i*i] + 1);
		}
	}

	cout << arr[n];

}