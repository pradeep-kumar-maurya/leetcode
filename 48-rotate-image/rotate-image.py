class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i, row in enumerate(matrix):

            j = i + 1

            while j < len(row):

                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp

                j += 1

        for row in matrix:
            i = 0
            j = len(row) - 1

            while i <= j:
                temp = row[j]
                row[j] = row[i]
                row[i] = temp
                i += 1
                j -= 1

        return matrix
