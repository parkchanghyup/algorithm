#include<iostream>
#include<vector>

using namespace std;

int result = 0;

void func(int a, int cnt, vector<int> numbers, int target) {
    
    //종료부
    if (cnt == numbers.size()) {
        //타겟과 일치하면 결과값 +1
        if (a == target) result++;
        return;
    }
    
    //양수로 보내기
    func(a + numbers[cnt], cnt + 1, numbers, target); 

    //음수로 보내기
    func(a - numbers[cnt], cnt + 1, numbers, target);

}

int solution(vector<int> numbers, int target) {
    func(0, 0,numbers, target);
    int answer = result;
    return answer;
}
