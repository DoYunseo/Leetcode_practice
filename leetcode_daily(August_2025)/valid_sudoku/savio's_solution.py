from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_col = defaultdict(list)
        seen_row = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit() and board[i][j] in seen_row[i]:
                    return False

                if board[i][j].isdigit() and board[i][j] in seen_col[j]:
                    return False

                seen_row[i].append(board[i][j])
                seen_col[j].append(board[i][j])
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()

                for row_off in range(3):
                    for col_off in range(3):
                        current = board[i + row_off][j + col_off]
                        if current == ".":
                            continue

                        if current in seen:
                            return False
                        seen.add(current)
        return True

        
        # now do the 3 * 3 block to check


        