import pygame

class Score:
    def __init__(self, size, pos):
        self.score = 0
        self.pos = pos
        self.font = pygame.font.SysFont(None, size)
    
    def update(self, val):
        self.score+=val
    
    def render(self, surf):
        score_text = self.font.render(str(self.score), False, (255, 255, 255))
        surf.blit(score_text, self.pos)