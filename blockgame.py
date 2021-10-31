import pygame
import sys
from pygame import sprite, Vector2
from settings import *
from camera import Camera

class Block(sprite.Sprite):
    def __init__(self, game, start, size=(1000, 40), color = red):
        sprite.Sprite.__init__(self, game.sprites, game.layer1)
        self.game = game
        self.rect = pygame.Rect(start[0], start[1], size[0], size[1])
        self.speed = 5*deltaConst
        self.vel = Vector2(self.speed, 0)
        self.color = color
        self.stopped = False
        self.render()
    
    def render(self):
        self.image = pygame.Surface(self.rect.size).convert_alpha()
        self.image.fill(self.color)
    
    def update(self):
        self.move()
        self.render()
        now = pygame.time.get_ticks()
        if not self.stopped and now-self.game.lastStopped > 300:
            if checkKey("stop"):
                self.vel.x = 0
                self.game.stopped()
                self.stopped = True
    
    def move(self):
        self.rect.move_ip(self.vel)
        if self.rect.right > winWidth or self.rect.left < 0:
            self.vel.x *= -1

class Game:

    def __init__(self):
        self.win = pygame.display.set_mode((winWidth, winHeight), pygame.HWSURFACE)
        self.startSize = (200, 40)
    
    def new(self):
        self.gameOver = False
        self.lastBlock = False
        self.lastStopped = pygame.time.get_ticks()
        self.score = 0
        self.clock = pygame.time.Clock()
        self.sprites = sprite.Group()
        self.layer1 = sprite.Group()
        self.layers = [self.layer1]
        self.cam = Camera(self)
        self.startBlock = Block(self, (0, 0), self.startSize)

    def refresh(self):
        self.win.fill(white)
        self.render()
        pygame.display.update()
    
    def render(self):
        for layer in self.layers:
            for s in layer:
                self.win.blit(s.image, self.cam.apply(s))
        
        if self.gameOver:
            gOver = fonts["gameover"].render("Game Over", True, orangeRed)
            self.win.blit(gOver, gOver.get_rect(center=self.win.get_rect().center).topleft)
        
        score = fonts["score"].render("Score: " + str(self.score), True, black)
        self.win.blit(score, score.get_rect(right=winWidth-10).topleft)

    def getCurrent(self):
        for s in self.sprites:
            if isinstance(s, Block):
                if not s.stopped:
                    self.currentBlock = s
                    break
    
    def update(self):
        self.getCurrent()
        self.sprites.update()

    def stopped(self):
        self.lastStopped = pygame.time.get_ticks()
        l = self.lastBlock
        self.getCurrent()
        c = self.currentBlock
        if l:
            w = min(l.rect.right, c.rect.right) - max(l.rect.left, c.rect.left)
            print(w)
            if w < 1:
                self.gameOver = True
            else:
                newSize = (w, 40)
                c.rect = pygame.Rect(max(l.rect.left, c.rect.left), c.rect.y, w, c.rect.height)
                self.score += 1
        else:
            newSize = self.startSize
            self.score += 1

        if not self.gameOver:
            self.lastBlock = c
            self.currentBlock = Block(self, (0, self.currentBlock.rect.y-40), newSize)

    def quit(self):
        pygame.quit()

    def main(self):
        while True:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                    break
            if self.gameOver:
                now = pygame.time.get_ticks()
                if checkKey('retry') and now - self.lastStopped > 200:
                    self.lastStopped = now
                    break 
            else:
                self.update()
            self.refresh()
    
    def run(self):
        while True:
            self.new()
            self.main()

if __name__ == '__main__':
    game = Game()
    game.run()
