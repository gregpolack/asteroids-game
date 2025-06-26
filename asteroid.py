from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            (255, 255, 255),
            (self.position.x, self.position.y),
            self.radius,
            width=2
            )
        
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        positive_vector = self.velocity.rotate(random_angle)
        negative_vector = self.velocity.rotate(-random_angle)

        split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, split_asteroid_radius)

        asteroid_one.velocity = positive_vector * 1.2
        asteroid_two.velocity = negative_vector * 1.2