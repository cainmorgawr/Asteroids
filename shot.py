from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_RADIUS, PLAYER_SHOOT_SPEED
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, angle):
        super().__init__(x, y, SHOT_RADIUS)
        self.angle = angle
        self.speed = PLAYER_SHOOT_SPEED

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", (int(self.position.x), 
                            int(self.position.y)), int(self.radius), LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt