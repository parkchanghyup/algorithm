#include<iostream>
#include<vector>

using namespace std;

int result= 0;

void func(int a, int cnt,vector<int> numbers,int target) {
	if (cnt == numbers.size()) {
		if (a == target) 	result++;
		return;
		
	}

	func(a + numbers[cnt], cnt + 1,numbers,target);
	func(a - numbers[cnt], cnt + 1, numbers, target);


}


int solution(vector<int> numbers, int target) {
	func(0, 0, numbers, target);
	int answer = result;
	return answer;
}

int main() {
	vector<int> a = { 1,1,1,1,1, };
	int ab = solution(a, 3);
	cout << ab;
}