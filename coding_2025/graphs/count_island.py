from typing import List


def count_island(matrix: List[List[int]]) -> int:
    if not matrix:
        return 0
    count = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 1:
                dfs(r, c, matrix)
                count +=1
    return count



def dfs(r: int, c: int, matrix: List[List[int]]) -> None:
    matrix[r][c] = -1
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for d in dirs:
        next_r = r + d[0]
        next_c = c + d[1]
        if (is_within_bounds(r,c, matrix) and matrix[r][c] == 1):
            dfs(next_r, next_c, matrix)



def is_within_bounds(r:int, c: int, matrix: List[List[int]]) -> bool:
    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])
