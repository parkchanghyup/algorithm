#include<iostream>
typedef long long ll;
using namespace std;

ll A, B, C;

ll func(ll a, ll b) {
	if (b == 1)return a % C;
	ll val = func(a, b / 2);
	val = (val * val) % C;
	if (b % 2)val = (val * a) % C;//b°¡ È¦¼ö.
	return val;
}



int main() {
	cin >> A >> B >> C;
	cout << func(A, B);

}