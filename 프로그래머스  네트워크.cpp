#include<iostream>
#include<vector>

using namespace std;

int visited[100];

//기본적인 dfs 구조
void dfs(int cur, int n, vector<vector<int>> computers) {
    visited[cur] = true;

    for (int i = 0; i < n; i++) {
        if (!visited[i] && computers[cur][i] == !]) dfs(i, n, computers);
    }
}


//dfs를 이용하여 컴포넌트의 갯수를 구함
int dfsAll(int n, vector<vector<int>>computers) {
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

    int answer = dfsAll(n, computers);
    return answer;
}