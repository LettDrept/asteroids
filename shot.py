# The player's shot objects in the game
from circleshape import *                   # imports base game shape
from constants import *                     # imports variables from constants

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        
        

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)