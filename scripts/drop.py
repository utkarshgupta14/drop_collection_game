import pygame
from scripts.entities import PhysicsEntity

class Drop(PhysicsEntity):
    def __init__(self, game, e_type, size, pos):
        super().__init__(game, e_type, size, pos, velocity=(0, 2))
    
    def check_collision(self, collision_area):
        drop_r = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        if drop_r.colliderect(collision_area):
            return True
        else:
            return False
    def check_boundary(self):
        if self.pos[1] >= self.game.display.get_size()[1]:
            return True
        else:
            return False
        