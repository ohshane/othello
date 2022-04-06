import random
from functools import reduce

import numpy as np

from misc import *


class Board:
    def __init__(self, matrix=MATRIX):
        matrix = list(map(lambda x: list(map(int, list(x))), matrix.split()))
        try:
            matrix = np.matrix(matrix, dtype=np.byte)
        except:
            raise Exception
        
        i, j = matrix.shape
        if i % 2 != 0 and j % 2 != 0:
            raise Exception

        self.matrix = matrix
        self.row = i
        self.col = j

    def visualize(self, verbose=False):
        if verbose:
            rows_2x2 = []
            for i in range(self.row-1):
                row_2x2 = []
                for j in range(self.col-1):
                    flat = self.matrix[i:i+2, j:j+2].flatten().tolist()
                    flat = list(map(bool, flat[0]))
                    if   flat == [0,0,0,1]: row_2x2.append('╔')
                    elif flat == [0,0,1,0]: row_2x2.append('╗')
                    elif flat == [0,1,0,0]: row_2x2.append('╚')
                    elif flat == [1,0,0,0]: row_2x2.append('╝')

                    elif flat == [1,1,1,0]: row_2x2.append('╔')
                    elif flat == [1,1,0,1]: row_2x2.append('╗')
                    elif flat == [1,0,1,1]: row_2x2.append('╚')
                    elif flat == [0,1,1,1]: row_2x2.append('╝')
                    
                    elif flat == [0,0,1,1]: row_2x2.append('╤')
                    elif flat == [1,1,0,0]: row_2x2.append('╧')
                    elif flat == [0,1,0,1]: row_2x2.append('╟')
                    elif flat == [1,0,1,0]: row_2x2.append('╢')
                    elif flat == [1,1,1,1]: row_2x2.append('┼')

                    elif flat == [1,0,0,1]: row_2x2.append('╬')
                    elif flat == [0,1,1,0]: row_2x2.append('╬')

                    else: row_2x2.append(' ')

                s = row_2x2[0]
                for j in range(1, self.col-1):
                    flat = self.matrix[i:i+2, j].flatten().tolist()
                    flat = list(map(bool, flat[0]))
                    if   flat == [1,0]: s += '═══'
                    elif flat == [0,1]: s += '═══'
                    elif flat == [1,1]: s += '───'
                    else: s += '   '
                    s += row_2x2[j]

                rows_2x2.append(s)
            
            rows = []
            for i in range(1, self.row-1):
                s = ''
                for j in range(self.col-1):
                    flat = self.matrix[i,j:j+2].flatten().tolist()
                    flat = list(map(bool, flat[0]))
                    if   flat == [0,1]: s += '║'
                    elif flat == [1,0]: s += '║'
                    elif flat == [1,1]: s += '│'
                    else: s += ' '

                row = s[0]
                for j in range(1, self.col-1):
                    item = self.matrix[i,j]
                    row += ' ' + ICON_VERBOSE[item] + ' '
                    row += s[j]
            
                rows.append(row)

            s = ' ' * 4
            for i in range(self.col-2):
                s += f'{str(i+1):^4}'
            s += '\n'
            for i in range(len(rows)):
                s += ' '*3 + rows_2x2[i] + '\n'
                s += f'{str(i+1):>2} ' + rows[i] + '\n'
            s += ' '*3 + rows_2x2[-1]

            return s
        
        else:
            s = self.matrix[1:self.row-1, 1:self.col-1].tolist()
            s = list(map(lambda row: [ICON[i] for i in row], s))
            s = reduce(lambda a, b: a+'\n'+b, map(lambda row: reduce(lambda a, b: a+' '+b, row, ''), s))
            return s