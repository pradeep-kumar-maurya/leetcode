class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # Below one takes extra space
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


        # Below one takes no extra space

        # rows = len(matrix)
        # cols = len(matrix[0])

        # for i in range(rows):
        #     for j in range(cols):

        #         if matrix[i][j] == 0:
        #             if isinstance(matrix[0][j], str):
        #                 matrix[0][j] = '0'
        #             else:
        #                 matrix[0][j] = 0
        #             matrix[i][0] = str(matrix[i][0])

        # for i in range(rows):
        #     for j in range(cols):

        #         if matrix[0][j] in ('0', 0):
        #             if isinstance(matrix[i][0], str):
        #                 matrix[i][j] = "0"
        #             else:
        #                 matrix[i][j] = 0

        # for i in range(rows):
        #     for j in range(cols):

        #         if isinstance(matrix[i][0], str):
        #             matrix[i][j] = '0'

        # for i in range(rows):
        #     for j in range(cols):

        #         if isinstance(matrix[i][j], str):
        #             matrix[i][j] = 0
