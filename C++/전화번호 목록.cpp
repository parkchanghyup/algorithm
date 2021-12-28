#include <string>
#include <vector>
#include <algorithm>
#include<iostream>
using namespace std;

bool solution(vector<string> phone_book) {
	bool answer = true;
	bool flag = false;
	for (int i = 0; i < phone_book.size(); i++) {
		for (int k = 0; k < phone_book.size(); k++) {

			if (i == k)continue;
			if (phone_book[i].length() > phone_book[k].length()) continue;
		
			for (int j = 0; j < phone_book[i].length(); j++) {

				if (phone_book[i][j] != phone_book[k][j]) {
					flag = true;
					continue;
				}

				
			}
			if (flag == true) {
				flag = false;
				continue;
			}

			answer = false;

			return answer;
		}
	}
	return answer;

}
int main() {
	vector<string> a = { "12","13" };
	bool result =solution(a);
	cout << result;

	
}