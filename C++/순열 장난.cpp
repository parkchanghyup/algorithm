#include<iostream>
#include<string>
#include<vector>

using namespace std;
string str;
int max_num, len;
int arr[51];
vector<int>v;


void func(int n) {
	//마지막 수열까지 확인했다면 출력 .
	if (n == len) {
		for (int i = 0; i < max_num; i++) {
			cout << v[i] << " ";
		}
		//한번만 출력
		exit(0);
	}
	int num;
	string s = "";
	//숫자를 한자리수 , 두자리수로 분할 .
	for (int i = n; i <= n + 1; i++) {
		
		s = s + str[i];
		num = stoi(s);
		//백트래킹 부분. 

		//숫자가 max_num 보다 크면 볼필요없음
		if (num > max_num) continue; 
		//앞에 이미 나온 숫자는 확인할 필요 없음 
		if (arr[num])continue;		
		v.push_back(num);
		arr[num] = 1;
		func(i + 1);
		arr[num] = 0;
		v.pop_back();

	}

}


int main() {
	cin >> str;
	len = str.length();

	if (len > 9)
		max_num = 9 + (len - 9) / 2;
	else
		max_num = len;

	for (int i = 1; i <= 50; i++)arr[i] = 0;

	func(0);
}