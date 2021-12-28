#include <iostream>
#include<algorithm>

using namespace std;

int arr[100001];
int k, n,coin[101];


int main() {
	cin >> n >> k;

	for (int i = 1; i <= k; i++) {
		arr[i] = 10001;
	}

	for (int i = 1; i <= n; i++) {
		cin >> coin[i];
		for (int j = coin[i]; j <= k; j++) {
			arr[j] = min(arr[j], arr[j - coin[i]] + 1);
		}
	}
	if (arr[k] == 10001) cout << -1;
	else cout<<arr[k];
}
