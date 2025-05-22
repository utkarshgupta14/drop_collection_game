import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, size, pos, velocity=(0, 0)):
        self.game = game
        self.type = e_type
        self.size = size
        self.pos = list(pos)
        
        self.velocity = list(velocity)
        
    def update_pos(self, movement=(0,0)):
        total_movement = (self.velocity[0] + movement[0], self.velocity[1] + movement[1])

        self.pos[0] += total_movement[0]
        self.pos[1] += total_movement[1]

    def render(self, screen):
        img = pygame.transform.scale(self.game.assets[self.type], self.size)
        screen.blit(img, self.pos)
    
