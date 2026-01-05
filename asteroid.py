from circleshape import CircleShape
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random
import pygame
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        asteroid_dir1 = self.velocity.rotate(angle)
        asteroid_dir2 = self.velocity.rotate(-angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid1.velocity = asteroid_dir1 * 1.2
        asteroid2.velocity = asteroid_dir2 * 1.2
        