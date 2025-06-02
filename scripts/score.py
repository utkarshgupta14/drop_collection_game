import pygame

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 16)
    
    def update(self, val):
        self.score+=val
    
    def render(self, surf):
        score_text = self.font.render(str(self.score), False, (255, 255, 255))
        surf.blit(score_text, (10, 10))