class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] == "0" or (i, j) in seen:
                return
            
            seen.add((i, j))
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in seen and grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

        return res

        