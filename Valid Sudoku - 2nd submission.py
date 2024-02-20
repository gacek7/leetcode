class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isValid(l):
            seen = set()
            for number in l:
                if number != '.':
                    if number in seen:
                        return False
                    seen.add(number)
            return True

        #check for rows and columns:
        for i in range(9):
            if not isValid(board[i]) or not isValid([board[j][i] for j in range(9)]):
                return False

        #check for sub-boxes:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not isValid(sub_box):
                    return False

        return True 

