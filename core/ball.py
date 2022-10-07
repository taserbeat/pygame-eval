import pygame
import typing as t


class Ball:
    def __init__(
        self,
        x: float = 200,
        y: float = 100,
        radius: float = 10,
        x_velocity=1,
        y_velocity=1,
        color: t.Tuple[int, int, int] = (0, 0, 255)
    ) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.color = color
        return

    def update(self, surface: pygame.surface.Surface):
        self.x += self.x_velocity
        self.y += self.y_velocity

        surface_rect = surface.get_bounding_rect()

        # 上辺の跳ね返り
        if self.y - self.radius <= surface_rect.top:
            self.y_velocity *= -1

        # 下辺の跳ね返り
        if self.y + self.radius >= surface_rect.bottom:
            self.y_velocity *= -1

        # 右辺の跳ね返り
        if self.x + self.radius >= surface_rect.right:
            self.x_velocity *= -1

        # 左辺の跳ね返り
        if self.x - self.radius <= surface_rect.left:
            self.x_velocity *= -1

        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
        return
