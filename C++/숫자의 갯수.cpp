#include<iostream>

using namespace std;


int main() {

	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int arr[10] = { 0,0,0,0,0,0,0,0,0,0 };

	long long a, b, c;
	cin >> a >> b >> c;
	long long num= a * b * c;

	while (1) {
		if (num / 10 == 0) {
			arr[num % 10]++;
			break;
		}
		arr[num % 10]++;
		num /= 10;
	}
	for (int i = 0; i < 10; i++)
		cout << arr[i] << "\n";


}