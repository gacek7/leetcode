import collections
import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        table_of_each_nines = []
        append_table = []

        for i in range(len(board)):
            for j in range(0, len(board[0]), 3):
                table_of_each_nines.append(board[i][j:j+3])

        for i in range(3):
            append_table.append(table_of_each_nines[i] + table_of_each_nines[i+3] + table_of_each_nines[i+6])
            append_table.append(table_of_each_nines[i+9] + table_of_each_nines[i+12] + table_of_each_nines[i+15])
            append_table.append(table_of_each_nines[i+18] + table_of_each_nines[i+21] + table_of_each_nines[i+24])

        for index in range(len(board)):

            counter = collections.Counter(board[index])
            for key, count in counter.items():
                if key.isdigit() and count > 1:
                    return False 

            counter_t = collections.Counter(np.transpose(board)[index])
            for key, count in counter_t.items():
                if key.isdigit() and count > 1:
                    return False 

            test_3x3 = collections.Counter(append_table[index])
            for key, count in test_3x3.items():
                if key.isdigit() and count > 1:
                    return False
        

        return True 

