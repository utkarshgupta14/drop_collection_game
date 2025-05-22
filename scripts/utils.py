import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path, colorkey=None):
    img_path = BASE_IMG_PATH+path
    img = pygame.image.load(img_path).convert()
    if colorkey is not None:
        img.set_colorkey(colorkey)
    return img