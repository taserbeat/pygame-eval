import pygame
import typing as t


class Sweeper:
    def __init__(
        self,
        x: int = 200,
        y: int = 300,
        width: int = 50,
        height: int = 10,
        x_velocity: int = 2,
        y_velocity: int = 2,
        color: t.Tuple[int, int, int] = (255, 0, 0)
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.color = color

        return

    def update(self, surface: pygame.surface.Surface):
        pressed_key = pygame.key.get_pressed()

        # 左キーの移動
        if pressed_key[pygame.K_LEFT]:
            self.x -= self.x_velocity
        # 右キーの移動
        elif pressed_key[pygame.K_RIGHT]:
            self.x += self.x_velocity
        # 上キーの移動
        elif pressed_key[pygame.K_UP]:
            self.y -= self.x_velocity
        # 下キーの移動
        elif pressed_key[pygame.K_DOWN]:
            self.y += self.y_velocity

        surface_rect = surface.get_bounding_rect()

        # 左の移動制限
        if self.x - self.width / 2 < surface_rect.left:
            self.x = surface_rect.left * self.width / 2

        # 右の移動制限
        if self.x + self.width / 2 > surface_rect.right:
            self.x = surface_rect.right - self.width / 2

        # 上の移動制限
        if self.y - self.height / 2 < surface_rect.top:
            self.y = surface_rect.top + self.height / 2

        # 下の移動制限
        if self.y + self.height / 2 > surface_rect.bottom:
            self.y = surface_rect.bottom - self.height / 2

        x_min = int(self.x - self.width / 2)
        y_min = int(self.y - self.height / 2)

        pygame.draw.rect(surface, self.color, (x_min, y_min, self.width, self.height))
        return
