import pygame

pygame.init()


# ウィンドウ作成
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("サンプルゲーム")

# 色の設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# メインループ
is_loop = True

while is_loop:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_loop = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            is_loop = False
        continue

    pygame.display.update()

pygame.quit()
