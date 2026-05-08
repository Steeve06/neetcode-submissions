class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Row,Col = len(matrix),len(matrix[0])

        topRow,botRow = 0, Row-1

        while topRow <= botRow:
            midRow = (topRow + botRow)//2

            if matrix[midRow][-1] < target:
                topRow += 1
            
            elif matrix[midRow][0] > target:
                botRow -= 1
            
            else:
                break

        midRow = (topRow + botRow)//2
        leftCol,rightCol = 0, Col-1

        while leftCol <= rightCol:
            midCol = (leftCol + rightCol)//2

            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] > target:
                rightCol -= 1
            elif matrix[midRow][midCol] < target:
                leftCol += 1

        return False






