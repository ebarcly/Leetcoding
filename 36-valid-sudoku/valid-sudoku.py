class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        box = [[False] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                cell_val = board[r][c]
                if cell_val == ".":
                    continue
                
                # convert to int and 0 based index
                num = int(cell_val) - 1

                # identify sub-grid
                box_index = (r // 3) * 3 + c // 3

                if rows[r][num] or cols[c][num] or box[box_index][num]:
                    return False
                
                rows[r][num] = True
                cols[c][num] = True
                box[box_index][num] = True
        
        return True