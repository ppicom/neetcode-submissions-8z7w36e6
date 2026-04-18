class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dfs(image, sr, sc, image[sr][sc], color)
        return image

def dfs(image, r, c, original_color, target_color):
    ROWS, COLS = len(image), len(image[0])

    if min(r, c) < 0:
        return
    if r == ROWS or c == COLS:
        return
    if image[r][c] != original_color:
        return
    if image[r][c] == target_color:
        return
    
    image[r][c] = target_color

    dfs(image, r+1, c, original_color, target_color)
    dfs(image, r-1, c, original_color, target_color)
    dfs(image, r, c+1, original_color, target_color)
    dfs(image, r, c-1, original_color, target_color)