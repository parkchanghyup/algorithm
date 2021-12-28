#include<iostream>
#include<stack>
using namespace std;

int main() {
    int N;
    scanf_s("%d", &N);
    stack<pair<int,int>> s;
    int num;
    for (int i = 1; i <= N; i++) {
        scanf_s(" %d", &num);
        if (i == 1) {
            s.push(make_pair(i, num));
            printf("0 ");
            continue;
        }
        
            while(!s.empty()){
            if (s.top().second < num) {
            s.pop();
            }
            else {
                printf("%d ", s.top().first);
                s.push(make_pair(i, num));
                break;
            }
            }

            if (s.empty()) {
                s.push(make_pair(i, num));
                printf("0 ");
            }
        
    }


}