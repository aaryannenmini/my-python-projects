import pygame

pygame.init()

#window variables
width,height=500,500
name = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game On")

#player variables
play_size=10
play_color=(50,176,62)
play_x=(width-play_size)//2
play_y=(height-play_size)
play_speed=5

#JUmping Variables
jumping=False
velocity = 0
g_force=0.5
j_strenght=-11

running= True
while running:
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
            running=False

    #mooing the cowawda
    key=pygame.key.get_pressed()    
    if key[pygame.K_d] and play_x < width-play_size:
        play_x += play_speed
    if key[pygame.K_a] and play_x>play_size:
        play_x -= play_speed
    if key[pygame.K_w] and play_y>play_size:
        play_y -= play_speed
    if key[pygame.K_s] and play_y < height-play_size:
        play_y += play_speed
#JUmping COncept
    if key[pygame.K_SPACE] and not jumping:
        jumping=True
        velocity=j_strenght

    #aplying gravity
    if jumping:
        play_y += velocity
        velocity+=g_force   #ancreasing downward velocity due to gravity
#preventing the ball from falling under the ground
    if play_y>height-(play_size*2):
        y=height-play_size
        jumping=False
        velocity=0
    name.fill((0,0,0))
    pygame.draw.circle(name,play_color,(play_x,play_y),play_size)
    pygame.display.update()
    pygame.time.Clock().tick(1000)


    
pygame.quit()  

