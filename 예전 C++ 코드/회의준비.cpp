#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
int N, M, arr[101][101], chk[101][101];
int check[101];


//컴포넌트 구하기
void bfs(int n, int num) {

	queue<int> q;
	q.push(n);
	check[n] = num;
	while (!q.empty()) {
		int x = q.front();
		q.pop();
		for (int i = 1; i <= N; i++) {
			if (chk[x][i] && !check[i]) {
				q.push(i);
				check[i] = num;
			}
		}

	}

}

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);


	cin >> N >> M;
	//배열 초기화
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			arr[i][j] = 987654321;
			chk[i][j] = 0;
		}
	}

	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		//컴포넌트를 구하기위해 배열을 두개만듦 상당히 비효율적  ㅠ 
		arr[a][b] = 1;
		arr[b][a] = 1;
		chk[a][b] = 1;
		chk[b][a] = 1;
	}
	int cnt = 0;

	//컴포넌트를 구해서 지정
	for (int i = 1; i <= N; i++) {
		if (!check[i]) {
			cnt++;
			bfs(i, cnt);
		}
	}


	//플루이드 와샬

	for (int k = 1; k <= N; k++) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j]);
			}
		}
	}

	int max_ans[101];
	for (int i = 0; i < 101; i++)max_ans[i] = 0;

	//각 인원마다 걸리는 의사전달시간 구하기.
	for (int k = 1; k <= cnt; k++) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (i == j)continue;
				if (check[i] == k) {
					if (check[j] == k)
						max_ans[i] = max(max_ans[i], arr[i][j]);
				}
			}
		}
	}


	cout << cnt<<"\n";
	vector<int> ans;

	//각 컴포넌트(위원회) 의 대표 구하기.
	for (int i = 1; i <= cnt; i++) {
		pair<int, int> result =make_pair(0, 987654321);
		for (int j = 1; j <= N; j++) {
			if (check[j] == i) {
				if (result.second > max_ans[j]) {
					result = make_pair(j, max_ans[j]);
				}
			}
		}
		ans.push_back(result.first);
	}

	//대표 오름차순 정렬
	sort(ans.begin(),ans.end());

	//대표 출력
	for (int i = 0; i < ans.size(); i++)
		cout << ans[i] << "\n";

}