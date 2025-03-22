'''
https://leetcode.com/problems/sparse-matrix-multiplication/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
'''

from collections import defaultdict

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # Dimensions
        m1, n1 = len(mat1), len(mat1[0])  # mat1: m1 x n1
        m2, n2 = len(mat2), len(mat2[0])  # mat2: m2 x n2

        # Initialize result matrix with zeros: shape m1 x n2
        res = [[0 for _ in range(n2)] for _ in range(m1)]

        # X[i][j] will store non-zero values of mat1 for row i
        X = [defaultdict(int) for _ in range(m1)]

        # Y[j][i] will store non-zero values of mat2 transposed: col j → row i
        Y = [defaultdict(int) for _ in range(n2)]

        # Build sparse representation of mat1
        for i in range(m1):
            for j in range(n1):
                if mat1[i][j] != 0:
                    X[i][j] = mat1[i][j]

        # Build sparse representation of mat2 (column-wise as row-wise)
        for i in range(m2):
            for j in range(n2):
                if mat2[i][j] != 0:
                    Y[j][i] = mat2[i][j]  # Notice: Y is accessed by [col][row] (transposed)

        # Multiply non-zero entries only
        for i in range(m1):          # For each row in mat1
            for j in range(n2):      # For each col in mat2
                for r in X[i]:       # For each non-zero col in mat1 row i
                    if r in Y[j]:    # If same index is non-zero in mat2 col j
                        res[i][j] += X[i][r] * Y[j][r]

        return res
