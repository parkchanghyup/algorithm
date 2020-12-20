#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;

int n, k;
int d[100001];  
int w[101], v[101];


void dp() {
	for (int i = 1; i <= n; i++) {
		for (int j = k; j >= 1; j--) {
			if (w[i] <= j) {
				d[j] = max(d[j], d[j - w[i]] + v[i]);  
			}
		}
	}

	cout << d[k] << "\n";
}

int main() {

	cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		cin >> w[i] >> v[i];
	}

	dp();

	
}