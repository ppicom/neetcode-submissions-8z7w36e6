class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        fresh = set()
        q = deque()
        neighs = [[1,0], [-1,0], [0,1], [0,-1]]

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        mins = 0
        while fresh and q:
            length = len(q)
            for _ in range(length):
                r, c = q.popleft()
                
                for dr, dc in neighs:
                    rdr, cdc = r+dr, c+dc
                    if min(rdr, cdc) < 0:
                        continue
                    if rdr == ROWS or cdc == COLS:
                        continue
                    if grid[rdr][cdc] == 1:
                        grid[rdr][cdc] = 2
                        q.append((rdr, cdc))
                        fresh.remove((rdr, cdc))
            mins += 1
        
        if fresh:
            return -1
        
        return mins