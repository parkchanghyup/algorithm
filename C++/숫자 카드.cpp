#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(0);

	int N;
	cin >> N;
	vector<int> v;
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		v.push_back(num);
	}

	sort(v.begin(), v.end());

	int M;
	cin >> M;

	for (int i = 0; i < M; i++) {
		int num;
		cin >> num;

		int low = 0, high = N - 1;
		bool pos = false;

		//ÀÌºÐ Å½»ö
		while (low <= high) {
			int mid = (low + high) / 2;
			if (v[mid] == num) {
				pos = true;
				break;
			}
			else if (v[mid] < num)low = mid + 1;
			else high = mid - 1;
		}

		if (!pos)
			cout << 0 << " ";
		else
			cout << 1 << " ";
	}
}