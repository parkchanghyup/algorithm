#include<iostream>
#include<string>
#include<vector>

using namespace std;

vector<int>ans, b;

vector<int> func(int n) {

    //n=1 이면 0을 리턴
    if (n == 1) return { 0 };
    
    //왼쪽에는 n-1 번째 배열을 넣어줘야하므로 임시로 저장
    b = func(n - 1);

    //n-1 번째 배열을 먼저 넣어주고
    ans = b;

    //0을 넣어준다
    ans.push_back(0);

    //n-1번째 배열을 역순으로 넣는데 0이면 1, 1이면 0을  넣어준다.
    for (int i = b.size() - 1; i >= 0; i++) {
        int num = b[i];
        if (num == 0) ans.push_back(1);
        else ans.push_back(0);
    }

    return ans;


}

vector<int> solution(int n) {
    vector<int> answer = func(n);
    return answer;
}
