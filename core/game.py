import pygame

from core.color import RGBColor
from core.ball import Ball
from core.sweeper import Sweeper


class Game:
    """
    ゲームクラス
    """

    def __init__(self) -> None:
        self.is_loop = False

        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("サンプル")

        self.ball = Ball()
        self.sweeper = Sweeper()

        self.clock = pygame.time.Clock()

        return

    def run(self):
        self.is_loop = True
        pygame.init()

        self.update()
        return

    def update(self):
        # https://qiita.com/ProOJI/items/56927105ceed4dd66ea3
        while self.is_loop:
            self.clock.tick(60)

            self.screen.fill(RGBColor.BLACK)

            self.ball.update(self.screen)
            self.sweeper.update(self.screen)

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
