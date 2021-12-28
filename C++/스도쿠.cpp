#include <iostream>
#include <vector>

using namespace std;


int sudoku[9][9];

bool row[9][10]; //열, 1~9
bool col[9][10]; //행, 1~9
bool square[9][10]; //3*3 박스 idx, 1~9

int change2SquareIdx(int y, int x)

{
	return (y / 3) * 3 + x / 3;
}

void DFS(int cnt)
{
	if (cnt == 81) //Sudoku는 총 81칸
	{
		for (int i = 0; i < 9; i++)
		{
			for (int j = 0; j < 9; j++)
				cout << sudoku[i][j] << " ";
			cout << endl;
		}
		exit(0); //답을 하나만 출력
	}


	int y = cnt / 9;
	int x = cnt % 9;


	if (sudoku[y][x]) //칸이 채워져있으면
		DFS(cnt + 1);
	else //채워져있지 않았고
	{
		for (int k = 1; k <= 9; k++)
		{
			//sudoku 규칙에 적합하면 채우고 본다
			if (!col[x][k] && !row[y][k] && !square[change2SquareIdx(y, x)][k])
			{
				sudoku[y][x] = k;
				col[x][k] = true;
				row[y][k] = true;
				square[change2SquareIdx(y, x)][k] = true;
				DFS(cnt + 1);
				sudoku[y][x] = 0;
				col[x][k] = false;
				row[y][k] = false;
				square[change2SquareIdx(y, x)][k] = false;
			}
		}
	}
}



int main(void)
{
	for (int i = 0; i < 9; i++)
	{
		for (int j = 0; j < 9; j++)
		{
			cin >> sudoku[i][j];
			if (sudoku[i][j])
			{
				col[j][sudoku[i][j]] = true;
				row[i][sudoku[i][j]] = true;
				square[change2SquareIdx(i, j)][sudoku[i][j]] = true;
			}
		}
	}

	DFS(0); //sudoku는 81칸

	return 0;
}