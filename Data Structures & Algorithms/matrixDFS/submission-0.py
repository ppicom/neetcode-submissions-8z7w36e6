class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return dfs(grid, 0, 0, set())

def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or # r or c out of bounds
        r == ROWS or c == COLS or # r or c out of bounds
        (r, c) in visit or # (r, c) already visited in this path
        grid[r][c] == 1): # (r, c) is not 'walkable'
        return 0
    
    if r == ROWS - 1 and c == COLS - 1: # we got to the target
        return 1
    
    visit.add((r, c))

    count = 0
    count += dfs(grid, r+1, c, visit)
    count += dfs(grid, r-1, c, visit)
    count += dfs(grid, r, c+1, visit)
    count += dfs(grid, r, c-1, visit)

    visit.remove((r, c))

    return count