class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_with_zero = set()
        cols_with_zero = set()
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):

            for j in range(cols):

                if matrix[i][j] == 0:
                    rows_with_zero.add(i)
                    cols_with_zero.add(j)

        for i in range(rows):

            for j in range(cols):

                if i in rows_with_zero:
                    matrix[i][j] = 0
                if j in cols_with_zero:
                    matrix[i][j] = 0
