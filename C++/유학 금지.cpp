#include<iostream>
#include<string>

using namespace std;



bool check(char c) {
	if(c=='C'|| c == 'A' || c == 'M' || c == 'B' || c == 'R' || c == 'I' || c == 'D' || c == 'G' || c == 'E'  ){
		return false;
	}
	return true;
}


int main() {
	string str;
	cin >> str;

	for (int i = 0; i < str.length(); i++) {
		if(check(str[i]))
			cout<<str[i];
	}
}