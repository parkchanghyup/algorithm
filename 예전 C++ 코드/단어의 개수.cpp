#include<iostream>
#include<string>

using namespace std;


int main() {
	string str;
	getline(cin, str);


	int result =0;
	//맨앞에 공백
	if (str[0] == ' ')result--;
	
	//맨뒤에 공백
	if (str[str.size() - 1] == ' ')result--;

	for (int i = 0; i < str.size(); i++) {
		if (str[i] == ' ')result++;
	}
	cout << result+1;

}