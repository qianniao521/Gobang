import  pygame

pygame.init()

screen_size = (960, 640)#显示画面尺寸
square_size = (screen_size[1] // 16, screen_size[1] // 16)#棋盘方格大小
piece_size = square_size[0] // 2#棋子半径尺寸
checkerboard_size = (square_size[0] * 15, square_size[1] * 15) #棋盘大小

piece_color = [(0, 0, 0), (255, 255, 255)]#棋子颜色
checkerboard_color = [(0, 200, 200), (0, 0, 0)]#棋盘颜色：背景、线条
bg_color = (200, 200, 200)

checkerboard_pos = (square_size[0] // 2, square_size[1] // 2)#棋盘坐标
guide_pos = (screen_size[1], screen_size[1] // 10)
result_pos = (screen_size[1], screen_size[1] * 8 // 10)


checkerboard_range = (checkerboard_pos[0], checkerboard_pos[1], checkerboard_size[0], checkerboard_size[1])#棋盘范围


font = pygame.font.SysFont("隶书", 48)
font_color = [(200, 0, 0), (60, 60, 60), (0, 0, 0), (200, 200, 200)]