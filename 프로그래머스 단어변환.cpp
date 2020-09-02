#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int use[1000];
int answer = 1000;


void DFS(string begin, string target, vector<string>words, int count) {

    int len = begin.length();
    int size = words.size();

    for (int i = 0; i < size; i++) {
        //이미사용한 문자면은 SKIP
        if (use[i])continue;

        string word = words[i];
        int cnt = 0;

        //글자가 다른 갯수를 센다 .
        for (int j = 0; j < len; j++) {
            if (word[j] != begin[j])cnt++;
        }

        //단어가 한글자만 다르다면
        if (cnt == 1) {

            //단어 변환 끝
            if (word == target) {
                answer = min(count + 1, answer);
                return;
            }

            use[i] = 1;
            DFS(words[i], target, words, count + 1);
            use[i] = 0;//백트래킹

        }
    }
}


int solution(string begin, string target, vector<string> words) {
    DFS(begin, target, words, 0);
    if (answer == 1000) return 0;
    return answer;
}

