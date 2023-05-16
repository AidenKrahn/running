import pygame, random, time

pygame.init()

window_width = 600
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
        
    def hit(self,win):
        bg = red
        win.fill(bg)
        pygame.time.delay(100)
        print('hit')
        
    
class Dodge(object):
    def __init__(self,width,height,color):
        dio = random.randint(1,4)
        if dio == 1:
            self.x = random.randint(10,590)
            self.y = 590
            self.facing = 1
            
        elif dio == 2:
            self.x = 590
            self.y = random.randint(10,590)
            self.facing = 2
            
        elif dio == 3:
            self.x = random.randint(5,590)
            self.y = 10
            self.facing = 3
            
        elif dio == 4:
            self.x = 10
            self.y = random.randint(10,590)
            self.facing = 4
            
        self.width = width
        self.height = height
        self.vel = 5
        self.color = color
        
    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

class Orb(Dodge):
    def __init__(self,width,height,x,y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vis = True
        self.color = blue
        
    def start(self,win):
        print('welcome')
        self.vis = False
        
    def froth(self,win):
        super().draw(win)
        
bg = white
good = True
grodd = Human(50,50,50,50,black)
loop = []
cold = Orb(50,50,250,250)
font1 = pygame.font.SysFont('timesnewroman', 20)
text = font1.render('Press keys to do random things!', 1, (255, 255, 255))
win.blit(text, (300 - (text.get_width()/2), 100))
text1 = font1.render('(ignore blue thing)', 1, (255, 255, 255))
win.blit(text1, (300 - (text.get_width()/2), 200))
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
    win.fill(bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            good = False
            break
        
    pygame.draw.rect(win,grodd.color,(grodd.x,grodd.y,grodd.width,grodd.height))
    if cold.vis == True:
        cold.froth(win)
    for loops in loop:
        loops.draw(win)
        if loops.facing == 1:
            if loops.y > 0:
                loops.y -= loops.vel
            
            else:
                loop.pop(loop.index(loops))
            
        elif loops.facing == 2:
            if loops.x > 0:
                loops.x -= loops.vel
                
            else:
                loop.pop(loop.index(loops))
            
        elif loops.facing == 3:
            if loops.y < 600:
                loops.y += loops.vel
                
            else:
                loop.pop(loop.index(loops))
            
        elif loops.facing == 4:
            if loops.x < 600:
                loops.x += loops.vel
                
            else:
                loop.pop(loop.index(loops))
                
        if loops.x > grodd.x and loops.x < grodd.x + grodd.width:
            if loops.y > grodd.y and loops.y < grodd.y + grodd.height:
                grodd.hit(win)
                loop.pop(loop.index(loops))
    if cold.vis == True:
        if cold.x + cold.width > grodd.x and cold.x < grodd.x + grodd.width:
            if cold.y + cold.height > grodd.y and cold.y < grodd.y + grodd.height:
                cold.start(win)
            
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
    
    if keys[pygame.K_v] and len(loop) < 5:
        loop.append(Dodge(5,5,black))
        
    if keys[pygame.K_j]:
        bg = green
        
    
    pygame.display.update()
    
pygame.quit()
