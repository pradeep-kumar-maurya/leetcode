class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):

                if matrix[i][j] == 0:
                    if isinstance(matrix[0][j], str):
                        matrix[0][j] = '0'
                    else:
                        matrix[0][j] = 0
                    matrix[i][0] = str(matrix[i][0])

        for i in range(rows):
            for j in range(cols):

                if matrix[0][j] in ('0', 0):
                    if isinstance(matrix[i][0], str):
                        matrix[i][j] = "0"
                    else:
                        matrix[i][j] = 0

        for i in range(rows):
            for j in range(cols):

                if isinstance(matrix[i][0], str):
                    matrix[i][j] = '0'

        for i in range(rows):
            for j in range(cols):

                if isinstance(matrix[i][j], str):
                    matrix[i][j] = 0
