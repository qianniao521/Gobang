
import sys
from model import *
from button import *

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()

    def start(self):
        self.model = Model()
        self.button = Button(self)

        while True:
            self.clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.load_checkerboard()
            self.load_piece(self.model.piece_list)
            self.load_guide()
            if self.model.win[0] == -1:
                self.button.action(events)
            else:
                self.load_win()
            pygame.display.update()


        pass

    def load_checkerboard(self):
        self.screen.fill(bg_color)
        pygame.draw.rect(self.screen, checkerboard_color[0], checkerboard_range, 0)
        for i in range(15):
            pygame.draw.line(self.screen, checkerboard_color[1],
                             (checkerboard_pos[0] + square_size[0] // 2,
                              checkerboard_pos[1] + (i + 0.5) * square_size[1]),
                             (checkerboard_pos[0] + checkerboard_size[0] - square_size[0] // 2,
                              checkerboard_pos[1] + (i + 0.5) * square_size[1]),
                             3)
        for i in range(15):
            pygame.draw.line(self.screen, checkerboard_color[1],
                             (checkerboard_pos[0] + (i + 0.5) * square_size[1],
                              checkerboard_pos[1] + square_size[1] // 2),
                             (checkerboard_pos[0] + (i + 0.5) * square_size[1],
                              checkerboard_pos[1] + checkerboard_size[1] - square_size[1] // 2),
                             3)


    def load_piece(self, piece_list):
        for piece in piece_list:
            m = piece.rank[0]
            n = piece.rank[1]
            x = checkerboard_pos[0] + int((n + 0.5) * square_size[0])
            y = checkerboard_pos[1] + int((m + 0.5) * square_size[1])
            pygame.draw.circle(self.screen, piece_color[piece.id], (x, y), piece_size, 0)  # 显示光标
        pass

    def load_guide(self):
        if self.model.piece == 0:
            surface = font.render("黑棋走！", False, font_color[2])
            self.screen.blit(surface, guide_pos)
        else:
            surface = font.render("白棋走！", False, font_color[2])
            self.screen.blit(surface, guide_pos)
        pass

    def load_win(self):
        if self.model.win[0] == 0:
            surface = font.render("黑棋胜！", False, font_color[0])
            self.screen.blit(surface, result_pos)
        else:
            surface = font.render("白棋胜！", False, font_color[0])
            self.screen.blit(surface, result_pos)
        pass


if __name__ == '__main__':
    game = Game()
    game.start()