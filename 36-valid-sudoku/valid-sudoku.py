class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize DS to store seen numbers for columns, rows, and 3x3 squares.
        cols = defaultdict(set)  # {(2): 5}
        rows = defaultdict(set)
        box = defaultdict(set)

        # Iterate through board
        for r in range(9):
            for c in range(9):
                # Get the value in the current cell
                current_val = board[r][c]

                # If cell is empty skip and move to next cell
                if current_val == ".":
                    continue

                box_index = (r // 3, c // 3)

                 # Check for duplicates
                if (
                    current_val in rows[r]
                    or current_val in cols[c]
                    or current_val in box[box_index]
                ):

                    return False

                # Add the number to the respective sets for future checks
                cols[c].add(current_val)
                rows[r].add(current_val)
                box[box_index].add(current_val)

        # Board is valid
        return True