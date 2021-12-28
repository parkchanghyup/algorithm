#include<iostream>
#include <string>
#include <vector>
#include<math.h>
using namespace std;

vector<int> solution(int brown, int red) {
	vector<int> answer;
	int sum = brown + red;
	int garo, sero;
	//i의 최소값은 3이고 최대값은 sqrt(sum)이다.( 약수의 최대값 )
	for (int i = 3; i <= sqrt(sum); i++) {
		//i가 sum의 약수이면
		if (sum % i == 0) {
			garo = i;
			sero = sum / i;
			if ((garo - 2) * (sero - 2) == red) {  // 레드카펫 의 넓이와 같으면
				answer.push_back(sero);
				answer.push_back(garo);
			}
		}

	}

	return answer;
}
int main() {
	vector<int>a = solution(3, 3);

	cout << a[0] << a[1];
}