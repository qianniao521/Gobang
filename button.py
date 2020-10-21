

from parameter import *
from pygame.locals import *
import pygame

class Button:
    def __init__(self, game):
        self.screen = game.screen
        self.model = game.model
        self.piece_list = game.model.piece_list
        self.pos0 = (checkerboard_range[0], checkerboard_range[1],
                     checkerboard_range[0] + checkerboard_range[2],
                     checkerboard_range[1] + checkerboard_range[3]) #(起始坐标pos_x, pos_y，终点坐标)
        self.square = self.model.square

    def action(self, events):
        point_x, point_y = pygame.mouse.get_pos()
        if self.pos0[0] < point_x < self.pos0[2] and self.pos0[1] < point_y < self.pos0[3]:#鼠标是否在棋盘上
            n = (point_x - self.pos0[0]) // square_size[0]
            m = (point_y - self.pos0[1]) // square_size[1]
            x = self.pos0[0] + int((n + 0.5) * square_size[0])
            y = self.pos0[1] + int((m + 0.5) * square_size[1])
            pygame.draw.circle(self.screen, (0, 200, 0), (x, y), 20, 4)#显示光标
            for event in events:    #放置棋子
                if event.type == MOUSEBUTTONUP:
                    self.model.add_piece((m, n), self.square)
                    # print((m, n))
                    break



            pass
        pass