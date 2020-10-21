from piece import *
import numpy as np

class Model:
    def __init__(self):
        self.piece_list = []
        self.win = [-1]
        self.piece = 0
        self.square = np.zeros((15, 15)) - 1

    def add_piece(self, rank, square):
        self.piece_list.append(Piece(self.piece, rank))
        square[rank[0]][rank[1]] = self.piece
        self.is_win(rank)
        self.piece = (self.piece + 1) % 2
        pass

    def is_win(self, rank):
        m = rank[0]
        n = rank[1]

        # 判断横着是否五子连珠
        i = j = 0
        while n - i - 1 >= 0:
            if self.square[m][n] == self.square[m][n - i - 1]:
                i +=1
            else:
                break
        while n + j + 1 <= 14:
            if self.square[m][n] == self.square[m][n + j + 1]:
                j += 1
            else:
                break
        if i + j == 4:
            self.win[0] = self.piece
            return

        # 判断竖着是否五子连珠
        i = j = 0
        while m - i - 1 >= 0:
            if self.square[m][n] == self.square[m - i - 1][n]:
                i += 1
            else:
                break
        while m + j + 1 <= 14:
            if self.square[m][n] == self.square[m + j + 1][n]:
                j += 1
            else:
                break
        if i + j == 4:
            self.win[0] = self.piece
            return

        # 判断斜（\）着是否五子连珠
        i = j = 0
        while m - i - 1 >= 0 and n - i - 1 >= 0:
            if self.square[m][n] == self.square[m - i - 1][n - i - 1]:
                i += 1
            else:
                break
        while m + j + 1 <= 14 and n + j + 1 <= 14:
            if self.square[m][n] == self.square[m + j + 1][n + j + 1]:
                j += 1
            else:
                break
        if i + j == 4:
            self.win[0] = self.piece
            return

        # 判断斜（/）着是否五子连珠
        i = j = 0
        while m - i - 1 >= 0 and n + i + 1 <= 14:
            if self.square[m][n] == self.square[m - i - 1][n + i + 1]:
                i += 1
            else:
                break
        while m + j + 1 <= 14 and n - j - 1 >= 0:
            if self.square[m][n] == self.square[m + j + 1][n - j - 1]:
                j += 1
            else:
                break
        if i + j == 4:
            self.win[0] = self.piece
            return




        pass