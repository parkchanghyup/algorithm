#include<iostream>
#include<algorithm>


using namespace std;
typedef long long ll;


int N, M;
int color[300001];
bool check(int n) {
	int num = 0;
	for (int i = 0; i < M; i++) {
		int a = color[i] / n;
		int b = color[i] % n;
		
		num += a;

		if (b) 	num ++;
	}
	if (num <= N)return true;
	return false;
}

int main() {

	cin >> N>>M;


	int high=0, low = 1;

	for (int i = 0; i < M; i++) {

		cin >> color[i];

		if (high < color[i]) 
			high = color[i];		
		
	}

	while (low <= high) {
		int mid = (low + high) / 2;

		bool pos = true;

		if (!check(mid)) pos = false;


		//보석이 남지않을때
		if (pos) high = mid - 1;

		//보석이 남을 때
		else  low = mid + 1;
			
		
	}
	cout << low;
	

}