#include<iostream>
#include<algorithm>

using namespace std;

int n;
int card[1001];
int arr[10001];


int main()
{
	cin >> n;

	for (int i = 1; i <= n; i++) {
		arr[i] = 0;
	}
	card[0] = card[1];

	for (int i = 1; i <= n; i++) {
		cin >> card[i];
		for (int j = i; j <= n; j++) {
			arr[j] = max(arr[j], arr[j - i] + card[i]);
		}

	}
	cout << arr[n];
}