#include <string>
#include <vector>
#include<iostream>
#include<math.h>
using namespace std;
int answer = 0;
int Size;
string a;
int arr[9999999] = { 0, };
int pri[9999999] = { 0, };
int idx_check[8];
bool prime(int n) { //소수구하기
    if (n < 2)return false;
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0)return false;
    }
    return true;
}
void check(int n,string str) { //숫자 만들기 
    if (str.length() == n) {
        if (prime(stoi(str))) { //stoi 함수 이용 .
            if (!arr[stoi(str)]) {
                answer++;
                arr[stoi(str)] = 1;
            }
        }
        return;
    }
    for (int i = 0; i < Size; i++) {
        if (idx_check[i])continue;
        idx_check[i] = 1;
        check(n, str + a[i]);
        idx_check[i] = 0;
    }
}
int solution(string numbers) {
    Size = numbers.size();
    a = numbers;
    for (int i = 1; i <= Size; i++) {
        check(i, "");
    }
    return answer;
}