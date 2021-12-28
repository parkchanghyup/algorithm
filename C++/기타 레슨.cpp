#include<iostream>
#include<vector>
#include<algorithm>
#include<string.h>

using namespace std;
typedef long long ll;

int main()
{
	int N, M;
	cin >> N >> M;
	vector<ll> blue(N);
	ll hi = 20;
	ll lo = 0;
	for (int i = 0; i < N; i++) {
		cin >> blue[i];
		lo = max(lo, blue[i]);
	}

	while (lo <= hi) {
		int cnt = 1;
		ll mid = (lo + hi) / 2;
		ll sum = blue[0];
		for (int i = 1; i < N; i++) {
			if (sum + blue[i] > mid) {
				cnt++;
				sum = 0;
			}
			sum += blue[i];
		}
		
		if (cnt <= M)
			hi = mid - 1;
		else
			lo = mid + 1;
		
	}
	cout << lo;
}
