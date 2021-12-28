#include<iostream>

using namespace std;

int main() {
	int x, y;
	cin >> x >> y;

	int day = 0;

	for (int i = x-1; i >=1; i--) {
		if ( i==1||i == 3 || i == 5 || i == 7 || i == 8 || i == 10 || i == 12)
			day += 31;
		else if (i == 2)
			day += 28;
		else
			day += 30;
	}

	day += y;
	day = day % 7;

	switch (day) {
	case 0:
		cout << "SUN";
		break;
	case 1:
		cout << "MON";
		break;
	case 2:
		cout << "TUE";
		break;
	case 3:
		cout << "WED";
		break;
	case 4:
		cout << "THU";
		break;
	case 5:
		cout << "FRI";
		break;
	default:
		cout << "SAT";
		break;
	}
	return 0;
}