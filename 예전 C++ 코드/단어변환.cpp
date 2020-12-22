#include<iostream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int use[1000];
int answer = 1000;

void DFS(string begin, string target, vector<string> words,int count) {

	int len = begin.length();
	int size = words.size();
	for (int i = 0; i < size; i++) {
		if (use[i])continue;
		string word = words[i];
		int cnt = 0;
		for (int j = 0; j < len; j++) {
			if (word[j] != begin[j]) cnt++;
		}
		if (cnt == 1) {
			if (word == target) {
				answer = min(count+1, answer);
				return;
			}
			use[i] = 1;
			DFS(words[i], target, words, count + 1);
			use[i] = 0;
		}
			
	}


}

int solution(string begin, string target, vector<string> words) {
	DFS(begin, target, words, 0);
	if (answer == 1000) return 0;
	return answer;
}

int main() {
	string a = "hit";
	string b = "cog";
	vector<string > c= { "hot","dot","dog","lot","log","cog" };
	int k = solution(a, b, c);
	cout << k;
}