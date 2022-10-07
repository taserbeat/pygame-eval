import pygame
import typing as t


class Sweeper:
    def __init__(
        self,
        x_min: int = 100,
        y_min: int = 100,
        width: int = 50,
        height: int = 10,
        x_velocity: int = 1,
        y_velocity: int = 1,
        color: t.Tuple[int, int, int] = (255, 0, 0)
    ) -> None:
        self.x_min = x_min
        self.y_min = y_min
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
            self.x_min -= self.x_velocity
        # 右キーの移動
        elif pressed_key[pygame.K_RIGHT]:
            self.x_min += self.x_velocity
        # 上キーの移動
        elif pressed_key[pygame.K_UP]:
            self.y_min -= self.x_velocity
        # 下キーの移動
        elif pressed_key[pygame.K_DOWN]:
            self.y_min += self.y_velocity

        surface_rect = surface.get_bounding_rect()

        # 左の移動制限
        if self.x_min < surface_rect.left:
            self.x_min = surface_rect.left

        # 右の移動制限
        if self.x_min + self.width > surface_rect.right:
            self.x_min = surface_rect.right - self.width

        # 上の移動制限
        if self.y_min < surface_rect.top:
            self.y_min = surface_rect.top

        # 下の移動制限
        if self.y_min + self.height > surface_rect.bottom:
            self.y_min = surface_rect.bottom - self.height

        pygame.draw.rect(surface, self.color, (self.x_min, self.y_min, self.width, self.height))
        return
