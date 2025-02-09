import pygame
import random

pygame.init()

height=500
width=650
screen_display=pygame.display.set_mode((width,height))
pygame.display.set_caption("Shooter")
clock=pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)
font_name=pygame.font.match_font("Times")

def draw_text(surface,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,white)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surface.blit(text_surface,text_rect)

class Player(pygame.sprite.Sprite):  # pygame.sprite.Sprite is a parent class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image1=pygame.image.load("sapceship.png").convert()
        self.image=pygame.transform.scale(self.image1,(100,100))
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.centerx=width/2
        self.rect.bottom=height-20
        self.speedx=0

    def update(self):
        self.speedx=0
        key=pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.speedx=-8 
        if key[pygame.K_d]:
            self.speedx=8
        self.rect.x+=self.speedx
        if self.rect.right>width:
            self.rect.right=width
        if self.rect.left<0:
            self.rect.left=0
    def shoot(self):
        bullet=Bullet(self.rect.centerx,self.rect.top)
        allsprite.add(bullet)
        bullets.add(bullet)
        #shootsound.play()  #uncommented if sound is added
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image1=pygame.image.load("astroid.png").convert() 
        self.image=pygame.transform.scale(self.image1,(60,60 ))
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,width-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedx=random.randrange(-3,3)
        self.speedy=random.randrange(2,8)
    def update(self):
        self.rect.x+=self.speedx
        self.rect.y+=self.speedy
        if self.rect.top>height+20 or self.rect.left<-25 or self.rect.right>width+25:
            self.rect.x=random.randrange(0,width-self.rect.width)
            self.rect.y=random.randrange(-100,-40)
            self.speedx=random.randrange(-3,3)
            self.speedy=random.randrange(2,8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image1=pygame.image.load("laser.png").convert() 
        self.image=pygame.transform.scale(self.image1,(80,80))
        self.image.set_colorkey(black)
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=-10
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()

#load ALl the gaming graphics

background1=pygame.image.load("background.png").convert_alpha()
background=pygame.transform.scale(background1,(650,500))
bgrect=background.get_rect()
#load sound
#shoootsound=pygame.mixer.Sound("typethenameofsoundfile")

#create sprite groups

allsprite=pygame.sprite.Group()
mobs=pygame.sprite.Group()
bullets=pygame.sprite.Group()

player=Player()#object for the player class
allsprite.add(player)

#creating mobs
for i in range(7):
    mob=Mob()#creating object for the mob class
    allsprite.add(mob)
    mobs.add(mob)
#gameloop
running=True
game_over=False

while running:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player.shoot()
    allsprite.update()

    #check f mob its the player
    hits=pygame.sprite.spritecollide(player,mobs,False,pygame.sprite.collide_rect)
    if hits:
        game_over=True
    
    #bullet touching thwe mob
    hits=pygame.sprite.groupcollide(mobs,bullets,True,True)
    for hit in hits:
        mob=Mob()         
        allsprite.add(mob)
        mobs.add(mob)

    #drawing allsprites
    screen_display.fill(black)
    screen_display.blit(background,bgrect)
    allsprite.draw(screen_display)

    if game_over:
        draw_text(screen_display,"Oh No",50,width//2,height//2)
        pygame.display.update()
        pygame.time.wait(2000)
        running=False

    pygame.display.update()

pygame.quit()