class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])
        topRow,botRow = 0, ROWS - 1

        while topRow <= botRow:
            midRow = (topRow + botRow)//2

            if target > matrix[midRow][-1]:
                topRow = midRow + 1
            elif target < matrix[midRow][0]:
                botRow = midRow - 1
            else:
                break

        midRow = (topRow + botRow)//2
        leftCol,rightCol = 0, COLS - 1
        while leftCol <= rightCol:
            midCol = (leftCol + rightCol)//2
            if target < matrix[midRow][midCol]:
                rightCol = midCol - 1
            elif target > matrix[midRow][midCol]:
                leftCol = midCol + 1
            else:
                return True
        return False



        