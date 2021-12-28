class Solution:
    def numIslands(self,grid: List[List[str]]) -> int:
        def dfs(y, x):
            if y < 0 or x < 0 or y >= len(grid) or x >= len(
                    grid[0]) or grid[y][x] != '1':
                return

            grid[y][x] = 0

            dfs(y + 1, x)
            dfs(y, x + 1)
            dfs(y - 1, x)
            dfs(y, x - 1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        return cnt  