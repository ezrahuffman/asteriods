from pickletools import pytuple

import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # abstract method
    def draw(self, screen):
        pass

    # abstract method
    def update(self, dt):
        pass

    def is_colliding(self, other):
        d = pygame.Vector2.distance_to(self.position, other.position)
        tot_radius = self.radius + other.radius
        return d <= tot_radius