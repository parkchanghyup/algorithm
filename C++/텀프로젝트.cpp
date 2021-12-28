#include<iostream>

using namespace std;

int N, cnt;
int line[100001];
bool visited[100001];
bool done[100001]; // 방문종료 여부

void DFS(int node) {

	visited[node] = 1;
	int next = line[node];
	//방문한적이없으면 재귀
	if (!visited[next]) DFS(next);
	
	//방문한적이 있는데 끝난노드가 아니다.->사이클을이룸
	else if (!done[next]) {
		
		
		//팀원의 수를샘 , for문 중요
		for (int i = next; i != node; i = line[i])cnt++;

		cnt++;

	}
	done[node] = 1;
}

void reset(int num) {
	for (int i = 0; i < num; i++) {
		visited[i] = 0;
		line[i] = 0;
		done[i] = 0;
	}
}
int main() {

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> N;
		reset(N);

		for (int j = 1; j <= N; j++) {
			cin >> line[j];
		}

		//팀을이룬사람의수
		cnt = 0;

		for (int j = 1; j <= N; j++) {
			if (!visited[j])
				DFS(j);
		}

		//팀을이루지못한 사람의수
		cout << N - cnt << endl;
	}
}