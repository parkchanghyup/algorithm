#include<iostream>
#include<vector>

using namespace std;

int visited[100];
void dfs(int cur, int n, vector<vector<int>> computers) {

	visited[cur] = true;

	for (int i = 0; i < n; i++) {
		if (!visited[i] && computers[cur][i] == 1) dfs(i, n, computers);
	}
}
int dfsAll(int n, vector<vector<int>> computers) {
	int components = 0;
	for (int i = 0; i < n; i++) {

		if (!visited[i]) {
			dfs(i, n, computers);
			components++;

		}
			
	}
	return components;
}
int solution(int n, vector<vector<int>> computers) {
	int answer = dfsAll(n,computers);
	return answer;
}



int main() {
	vector<vector<int>> graph = { {1, 1, 0}, {1, 1, 0}, {0, 0, 1} };
	vector < vector<int>> graph1 = { {1, 1, 0}, {1, 1, 1}, {0, 1, 1} };

	cout << solution(3, graph) << '\n';
	memset(visited, false, sizeof(visited));
	cout << solution(3, graph1) << '\n';

}