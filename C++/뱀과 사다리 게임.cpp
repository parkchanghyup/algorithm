#include<iostream>
#include<vector>
#include<queue>


using namespace std;
typedef pair<int, int>  p;
vector<p> v;
int N, M, visited[101], result = 0;

int number(int n) {

	//뱀이나 사다리를 만나면 
	for (int i = 0; i < N + M; i++) {
		if (v[i].first == n)return v[i].second;
	}

	//안 만나면
	return n;

}

void bfs() {
	queue<int> q;
	visited[1] = 1;
	q.push(1);
	while (!q.empty()) {
		int Size = q.size();
		
		for (int i = 0; i < Size; i++) {
			int x = q.front();
			q.pop();

			//갈수있는 칸 다넣어
			for (int j = 1; j <= 6; j++) {
				if (x + j <= 100 && !visited[x + j]) {
					int y = number(x + j);
					q.push(y);
					visited[y]=1;
				}
			}

			if (visited[100])return;
		}
		result++;
	
	}


}


int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	cin >> N >> M;

	for (int i = 0; i < N + M; i++) {
		int a, b;
		cin >> a >> b;
		v.push_back(p(a, b));
	}
	bfs();
	cout << result+1;


}