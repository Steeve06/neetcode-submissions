class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        - create 3 hashmaps, col,rows and squares (each 3by3)
        - Iterate in all the rows and cols. They both have size 9
        - Check if elmt at board[r][c] was found in
        - Col, Row, or squares. Squares is given by R//3 and C//3
        - If found, return false reset the hashmaps 
        - return True
        
        """

        column = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in column[c] or board[r][c] in row[r] or board[r][c] in square[(r//3,c//3)]):
                    return False
                square[(r//3,c//3)].add(board[r][c])
                row[r].add(board[r][c])
                column[c].add(board[r][c])

        return True
       