#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

int N, M;

int start, destination;
vector<pair<int, int>> V[100001];
int visited[100001];

bool BFS(int cost) {
	queue<int> q;
	q.push(start);
	visited[start] = 1;

	while (!q.empty()) {
		int  curr = q.front();
		q.pop();

		//목적지 까지 갈 수있다면 return true 
		if (curr == destination) return true;

		for (int i = 0; i < V[curr].size(); i++) {
			int next = V[curr][i].first;
			int next_cost = V[curr][i].second;


			//중량 제한이 cost 일때 다리를 건널 수있는 것 만 탐색
			if (!visited[next] && cost <= next_cost) {
				visited[next] = true;
				q.push(next);
			}
		}

	}
	//목적지까지 가지 못하면 return false;
	return false;
}

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int result = 0;
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;

		//양방향 그래프 삽입
		V[a].push_back(make_pair(b, c));
		V[b].push_back(make_pair(a, c));

		result = max(result, c);

	}

	cin >> start >> destination;



	//이진 탐색

	int low = 0, high = result;

	while (low <= high) {
		//배열 초기화
		for (int i = 0; i <= N; i++)visited[i] = 0;
		int mid = (low + high) / 2;

		if (BFS(mid))
			low = mid + 1;
		else
			high = mid - 1;

	}
	cout << high;
}