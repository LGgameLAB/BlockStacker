import pygame, os

blue = (0, 0, 128)
black = (0,0,0)
white = (255,255,255)
shadow = (192, 192, 192)
white = (255, 255, 255)
lightGreen = (0, 255, 0)
green = (0, 200, 0)
darkGreen = (0, 100, 0)
yellow = (255,255,0)
blue = (0, 0, 128)
grey = (169, 169, 169)
lightBlue = (0, 0, 255)
cyan = (50, 255, 255)
red = (200, 0, 0)
lightRed = (255, 100, 100)
purple = (102, 0, 102)
orangeRed = (255,69,0)

keySet = {'stop': pygame.K_SPACE, 'retry': pygame.K_SPACE}

def checkKey(move):
    keys = pygame.key.get_pressed()
    if isinstance(move, str):
        try:
            for k in keySet[move]:
                if keys[k]:
                    return True
        except TypeError:
            if keys[keySet[move]]:
                return True
    return False

winWidth, winHeight = 500, 600
FPS = 60
delta = 1/FPS
deltaConst = delta/(1/60)

# ASSETSPATH = 
# def asset(assetName):
#     global ASSETSPATH

#     return os.path.join(ASSETSPATH, assetName)

if not __name__ == '__main__':
    pygame.font.init()
    fonts = {
        'gameover':pygame.font.SysFont('Comic Sans MS', 23),
        'score': pygame.font.SysFont('Comic Sans MS', 23)
    }