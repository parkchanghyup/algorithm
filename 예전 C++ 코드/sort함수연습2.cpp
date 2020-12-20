#include <iostream>

using namespace std;

int main() {

	int temp;
	int count[6];
	int array[30] = { 1,3,2,4,3,2,5,3,1,2,3,4,4,3,5,1,2,3,5,4,2,4,5,1,3,5,1,2,3 };

	for (int i = 1; i <= 5; i++) {
		count[i] = 0;
	}
	for (int i = 0; i < 30; i++) {
		count[array[i]]++;
	}

	for (int i = 1; i <= 5; i++) {
		if (count[i] != 0) {
			for (int j = 0; j < count[i]; j++) {
				cout << i;
			}
		}
	}
}