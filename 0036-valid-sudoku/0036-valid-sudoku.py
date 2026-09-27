class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_dict = {}
        col_dict = {}
        box_dict = {}
        for i in range(9):
            row_dict[i] = set()
            col_dict[i] = set()
        for i in range(3):
            for j in range(3):
                box_dict[(i, j)] = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    if (board[i][j] not in row_dict[i]) and (board[i][j] not in col_dict[j]) and (board[i][j] not in box_dict[(i//3, j//3)]):
                        row_dict[i].add(board[i][j])
                        col_dict[j].add(board[i][j])
                        box_dict[(i//3, j//3)].add(board[i][j])
                        print(board[i][j] + " is a valid addition to the board")
                    else:
                        return False
        return True
        