#include string
#include vector
#includealgorithm
using namespace std;

int solution(vectorvectorint triangle) {

    int dp[505][505];
    int size = triangle.size();
    vectorint  t;

    dp[1][0] = triangle[0][0] + triangle[1][0];
    dp[1][1] = triangle[0][0] + triangle[1][1];

    for (int i = 2; i  size; i++) {

        int Size = triangle[i].size();

        for (int j = 0; j  Size; j++) {

            맨왼쪽
            if (j == 0) dp[i][j] = dp[i - 1][j] + triangle[i][j];

            맨오른쪽
            else if (j == Size - 1) dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];

            그 외 중간 부분
            else
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] )+ triangle[i][j];

        }
    }

    마지막행에서 최대값을출력
    int answer = 0;
    int Size = triangle[size - 1].size();

    for (int i = 0; i  Size; i++) {
        answer = max(dp[size - 1][i], answer);
    }

    return answer;
}

