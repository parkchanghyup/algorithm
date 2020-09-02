#include <string>
#include <vector>
#include<iostream>
#include<algorithm>
using namespace std;
bool func(string a, string b) {
    return a + b > b + a;
}
string solution(vector<int> numbers) {
    int Size = numbers.size();
    vector <string> str;
    string answer;
    for (int i = 0; i < Size; i++)
        str.push_back(to_string(numbers[i]));
    
    sort(str.begin(), str.end(),func);
    if (str[0] == "0") return "0";
        for (int i = 0; i < Size; i++) {
            answer += str[i];
    }
    return answer;
}
