from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        collumns = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for collumn in range(9):
                if board[row][collumn] == ".":
                    continue
                
                if board[row][collumn] in rows[row]:
                    return False
                rows[row].add(board[row][collumn])

                if board[row][collumn] in collumns[collumn]:
                    return False
                collumns[collumn].add(board[row][collumn])

                square = (row // 3) * 3 + (collumn // 3)
                if board[row][collumn] in squares[square]:
                    return False
                squares[square].add(board[row][collumn])
        return True
                

# (row // 3) * 3 + (collumn // 3) 

