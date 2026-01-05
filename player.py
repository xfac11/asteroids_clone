from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import LINE_WIDTH
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot
import pygame
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        self.shot_cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        up = pygame.Vector2(0.0, 1.0)
        player_dir = up.rotate(self.rotation)
        player_dir *= PLAYER_SPEED * dt
        self.position += player_dir

    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        up = pygame.Vector2(0, 1)
        player_dir = up.rotate(self.rotation)
        shot.velocity = player_dir * PLAYER_SHOOT_SPEED

    
