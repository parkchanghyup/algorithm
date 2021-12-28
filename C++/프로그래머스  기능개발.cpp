#include<string>
#include<vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> complete;

    for (int i = 0; i < progresses.size(); i++) {
        //몇일 후 완료되는지 
        int day = (100 - progresses[i]) % speeds[i];

        //딱 맞아 떨어질때
        if (day == 0) complete.push_back((100 - progresses[i]) / speeds[i]);
        //나머지가 발생할때는 +1
        else
            complete.push_back((100 - progresses[i]) / speeds[i] + 1);
    }
    int high = complete[0];
    int cnt = 1;
    for (int i = 1; i < progresses.size(); i++) {
        //첫째날 기능보다 먼저 개발된경우
        if (high >= complete[i]) {
            cnt++;

            //마지막기능인경우 답에 푸쉬
            if (i == progresses.size() - 1)answer.push_back(cnt);
        }
        else {
            answer.push_back(cnt);
            //날짜갱신
            high = complete[i];
            cnt = 1;
            //마지막기능인경우 답에 푸쉬
            if (i == progresses.size() - 1)answer.push_back(cnt);
        }
    }
    return answer;
}
