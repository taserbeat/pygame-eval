import pygame

from core.color import RGBColor


class Game:
    """
    ゲームクラス
    """

    def __init__(self) -> None:
        self.is_loop = False

        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("サンプル")
        return

    def run(self):
        self.is_loop = True
        pygame.init()

        self.update()
        return

    def update(self):
        while self.is_loop:
            self.screen.fill(RGBColor.BLACK)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_loop = False

                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.is_loop = False

                continue

            continue

        return

    def quit(self):
        pygame.quit()
        return
