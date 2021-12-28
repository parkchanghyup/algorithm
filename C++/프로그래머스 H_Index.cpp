#include<iostream>
#include <string>
#include <vector>
#include<algorithm>
using namespace std;
int solution(vector<int> citations) {
    vector<int> num = citations;
    sort(num.begin(), num.end(),greater<int>()); //오름차순 정렬
    int target = num[0];
    for (int i = num[0]; i > 0;i--) {
        int cnt = 0;
        for (int j = 0; j < num.size(); j++) {
            if (num[j] >= i) cnt++;
        }
        if (cnt >= i) return i;
    }
    
    
    
}
int main() {
    vector<int> a = { 3,0,6,1,5 };
    int result = solution(a);
    cout << result;
}