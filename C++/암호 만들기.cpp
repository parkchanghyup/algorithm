#include<iostream>
#include<algorithm>
using namespace std;
int L, C;
char arr[16];


void func(int idx,int moum,int jaum,string str) {
	if (str.length() == L) {
		if (moum >= 1 && jaum >= 2) {
			cout << str<<"\n";
			
			return;
		}
		return;
	}
	for (int i = idx; i < C; i++) {
		string s = str;
		s.push_back(arr[i]);
		if (arr[i] == 'a' || arr[i] == 'e' || arr[i] == 'i' || arr[i] == 'o' || arr[i] == 'u') {
			
			func(i+ 1, moum + 1, jaum, s);
		}
		else {
			func(i + 1, moum, jaum + 1, s);
		}
	}
	return;

}





int main() {
	cin >> L >> C;
	
	for (int i = 0; i < C; i++) cin >> arr[i];
	sort(arr, arr + C);
	func(0, 0, 0, "");
	
}


