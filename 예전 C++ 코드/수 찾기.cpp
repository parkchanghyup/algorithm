#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	cin.tie(NULL);
	ios_base::sync_with_stdio(false);
	int N, M;
	int arr[100001];


	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> arr[i];

	sort(arr, arr + N);
	cin >> M;
	for (int i = 0; i < M; i++) {
		int num;
		cin >> num;
		int lo = 0;
		int hi = N - 1;
		bool pos = false;

		while (lo <= hi) {
			int mid = (lo + hi) / 2;

			if (num == arr[mid]) {
				pos = true;
				cout << 1;
				break;
			}
			else if (num < arr[mid]) hi = mid - 1;
			else lo = mid + 1;

		}
		if (!pos) cout << 0;
		cout << "\n";

	}

	return 0;


}