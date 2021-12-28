#include<string>
#include<vector>
#include<algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {

    vector<int> answer;

    int size = commands.size();

    for (int i = 0; i < size; i++) {

        int a = commands[i][0];
        int b = commands[i][1];
        int c = commands[i][2];

        vector<int> arr;

        //a번재 부터 b번째 까지자르고
        for (int j = a - 1; j < b; j++) {
            int num = array[j];
            arr.push_back(num);            
        }

        //정렬하여 c번째 숫자를 출력
        sort(arr.begin(), arr.end());
        answer.push_back(arr[c - 1]);
    }

    return answer;
}
