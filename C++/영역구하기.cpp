#include <stdio.h>

void main(void)
{
	int x = 0, y = 0;
	int perimeter = 0, area = 0;
	printf("사각형의 가로와 세로의 길이를 각각 입력해 주세요- >");// “사각형의 가로와 세로의 길이를 각각 입력해 주세요->”를 출력합니다.
	
	scanf("%d ", &x); // 이 곳에서 가로와 세로의 길이를 입력 받습니다.
	scanf("%d ", &y);

	printf("사각형의 둘레는 %d 이고, 넓이는 %d입니다.", x + x + y + y, x * y);// 사각형의 둘레와 넓이를 계산합니다.
	
	return;   // 계산 결과를 출력합니다.
}