import pygame

pygame.init()

window_width = 800
window_height = 600
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("POOP (python object oriented programming)")

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

class Human(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        
    def draw(self,win):
        pass
        
        
good = True
grodd = Human(0,0,50,50)
while good == True:
    win.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            good = False
            
    pygame.draw.rect(win,black,(grodd.x,grodd.y,grodd.width,grodd.height))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and grodd.x > grodd.vel:
        grodd.x -= grodd.vel
        
    elif keys[pygame.K_RIGHT] and grodd.x < window_width - grodd.width - grodd.vel:
        grodd.x += grodd.vel
        
    if keys[pygame.K_UP] and grodd.y < grodd.vel:
        grodd.y -= grodd.vel
        
    elif keys[pygame.K_DOWN] and grodd.y < window_height - grodd.width - grodd.vel:
        grodd.y += grodd.vel
    
    pygame.display.flip
    
pygame.quit()