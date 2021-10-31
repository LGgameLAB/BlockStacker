import pygame
from pygame import sprite
from settings import *

class Camera(sprite.Sprite):

    def __init__(self, game, width=winWidth, height=winHeight):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        self.game = game
        sprite.Sprite.__init__(self, game.sprites)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def applyRect(self, rect):
        return rect.move(self.camera.topleft)
        
    def update(self):
        self.target = self.game.currentBlock
        x = 0#x = -self.target.rect.centerx + int(winWidth / 2)
        y = -self.target.rect.centery + int(winHeight / 2)

        self.camera = pygame.Rect(x, y, self.width, self.height)