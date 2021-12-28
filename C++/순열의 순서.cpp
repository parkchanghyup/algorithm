#include<iostream>
#include<vector>
using namespace std;


int N, num;
vector<int> v,ans;

int check[21];
long long factorial[21],cnt=0,k;

int main() {


	cin >> N;
	factorial[0] = 1;
	//팩토리얼을 미리계산
	for (int i = 1; i < 21; i++) {
		factorial[i] = factorial[i - 1] * i;
	}

	cin >> num;
	//문제 1번
	if (num == 1) {
		cin >> k;
		for (int i = 0; i < N; i++) {
			for (int j = 1; j <= N; j++) {
				//이미 사용한 숫자는 continue
				if (check[j]) continue;
				//팩토리얼 수가 k 보다 작으면 k를 factorial 만큼 줄임
				if (factorial[N - 1-i] < k) {
					k = k - factorial[N - 1-i];
				}
				else {
					//팩토리얼 수가 k보다 크거나 같으면 출력벡터에 push.
					ans.push_back(j);
					check[j] = 1;
					break;
				}
			}
		}
		
		for (int i = 0; i < ans.size(); i++) {
			cout << ans[i] << " ";
		}

	}
	//문제 2번
	else {
		for(int i = 0 ;i<N;i++){
			int k;
			cin >> k;
			v.push_back(k);
		}
		for (int i = 0; i < N; i++) {
			for (int j = 1; j < v[i]; j++) {
				if (!check[j]) {
					cnt += factorial[N - i - 1];
				}			
			}
			check[v[i]] = 1;
		}
		cout << cnt + 1;


	}



}