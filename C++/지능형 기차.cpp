#include<iostream>
#include<algorithm>
using namespace std;

int main() {
	int sum=0;
	int max_sum=0;
	for (int i = 0; i < 4; i++) {
		int a, b;
		
			cin >> a >> b;
			sum = sum - a + b;
	
		max_sum = max(max_sum, sum);
	}
	cout << max_sum;
}