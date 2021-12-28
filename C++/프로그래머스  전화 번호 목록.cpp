#include<string>
#include<vector>
#include<algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    bool flag = false;
    for (int i = 0; i < phone_book.size(); i++) {
        for (int k = 0; k < phone_book.size(); k++) {
            //자기자신은 SKIP
            if (i == k)continue;

            //자기보다 길이가 짧으면 SKIP
            if (phone_book[i].length() > phone_book[k].length()) continue;

            for(int j = 0;j<phone_book[i].length();j++){
            
                if (phone_book[i][j] != phone_book[k][j]) {
                    flag = true;
                    continue;
                }            
            
            }
            
            if (flag) {
                flag = false;
                continue;
            }

            //접두어인 경우 
            answer = false;
            return answer;
        }
    }
    return answer
}
