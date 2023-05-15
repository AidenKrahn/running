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
yellow = (255,255,0)
orange = (255,128,0)
purple = (153,0,153)

class Human(object):
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.color = color
        
    def draw(self,win):
        pass
        
        
good = True
grodd = Human(50,50,50,50,black)
font1 = pygame.font.SysFont('timesnewroman', 30)
text = font1.render('Press keys to do random things!', 1, (255, 255, 255))
win.blit(text, (400 - (text.get_width()/2), 100))
pygame.display.update()
i = 0
while i < 200:
    pygame.time.delay(10)
    i += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            i = 301
            pygame.quit()

while good == True:
    pygame.time.delay(30)
    win.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            good = False
            
    pygame.draw.rect(win,grodd.color,(grodd.x,grodd.y,grodd.width,grodd.height))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and grodd.x > grodd.vel:
        grodd.x -= grodd.vel
        
    elif keys[pygame.K_RIGHT] and grodd.x < window_width - grodd.width - grodd.vel:
        grodd.x += grodd.vel
        
    if keys[pygame.K_UP] and grodd.y > grodd.vel:
        grodd.y -= grodd.vel
        
    elif keys[pygame.K_DOWN] and grodd.y < window_height - grodd.width - grodd.vel:
        grodd.y += grodd.vel
        
    if keys[pygame.K_b]:
        grodd.color = blue
        
    if keys[pygame.K_r]:
        grodd.color = red
        
    if keys[pygame.K_g]:
        grodd.color = green
        
    if keys[pygame.K_f]:
        grodd.width += 1
        
    if keys[pygame.K_d]:
        grodd.height += 1
        
    if keys[pygame.K_w]:
        grodd.width += 1
        grodd.height += 1
        
    if keys[pygame.K_a]:
        grodd.width -= 1
        
    if keys[pygame.K_s]:
        grodd.height -= 1
        
    if keys[pygame.K_q]:
        grodd.width -= 1
        grodd.height -= 1
        
    if keys[pygame.K_y]:
        grodd.color = yellow
        
    if keys[pygame.K_o]:
        grodd.color = orange
        
    if keys[pygame.K_p]:
        grodd.color = purple
        
    if keys[pygame.K_h]:
        grodd.color = white
        
    if keys[pygame.K_l]:
        grodd.color = black
        
    if keys[pygame.K_x]:
        break
    
    pygame.display.update()
    
pygame.quit()
