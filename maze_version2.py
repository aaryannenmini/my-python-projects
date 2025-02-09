import pygame
pygame.init()

width=600
height=400
screen_color=(155,155,155)
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Maze")

#variables

#player variable
player_x=50
player_y=50
player_size=30
player_speed=20
player_color=(0,0,255)

#Goa variables
score=0
goal_x=550
goal_y=350
goal_size=30
goal_color=(255,0,0)

#wall list x,y,width,height

walls=[
    (100,0,20,300),
    (200,100,20,300),
    (300,0,20,300),
    (400,100,20,300),
    (500,0,20,300)
]
wall_color=(0,0,255)
text_color=(255,0,0)

coins=[
    (150,50,20,20),
    (250,100,20,20),
    (350,0,20,20)
    
]
coin_color=(100,8,165)

#x,y,w,h,mx_speed,y_speed
obstocles=[
[180,200,20,20,3,2],
[380,200,20,20,3,-2]

]

ob_collor=(255,215,0)
running=True
vin=False
game_over=False
messagetime=0
font=pygame.font.SysFont("Hobo",60)
clock=pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    keys=pygame.key.get_pressed()

    if keys[pygame.K_a] and player_x>0:
        player_x-=player_speed
    if keys[pygame.K_d] and player_x < width-player_size:
        player_x+=player_speed

    if keys[pygame.K_w] and player_y> 0:
        player_y-=player_speed
    if keys[pygame.K_s] and player_y<height-player_size:
        player_y+=player_speed

    player=pygame.Rect(player_x,player_y,player_size,player_size)

    for wall in walls:
        wallrect=pygame.Rect(wall)
        if player.colliderect(wallrect):
            if keys[pygame.K_a]:
                player_x+=player_speed
            if keys[pygame.K_d]:
                player_x-=player_speed
            if keys[pygame.K_w]:
                player_y+=player_speed
            if keys[pygame.K_s]:
                player_y-=player_speed

    collected_coins=[]
    for y in coins:
        coinrect=pygame.Rect(y)
        if player.colliderect(coinrect):
            score=score+10
            collected_coins.append(y)
    coins=[coin for coin in coins if coin not in collected_coins]

    for obstocle in obstocles:
        obstocle[0]+=obstocle[4]
        obstocle[1]+=obstocle[5]#moving ibstacle with x,y
    #obstocles biunucng      of obsatcle
        if obstocle[0] <= 0 or obstocle[0] + obstocle[2] >= width:
            obstocle[4]= -obstocle[4] #reverse direction
        
        if obstocle[1] <= 0 or obstocle[1] + obstocle[3] >= height:
            obstocle[5]= -obstocle[5]

    for obstocle in obstocles:
        obstoclerect=pygame.Rect(obstocle[0],obstocle[1],obstocle[2],obstocle[3])
        if player.colliderect(obstoclerect):
            game_over=True
            messagetime=pygame.time.get_ticks()
            break



    goalrect=pygame.Rect(goal_x,goal_y,goal_size,goal_size)
    if player.colliderect(goalrect) and not vin:
        vin=True
        messagetimetime=pygame.time.get_ticks()#To record the time when the player wins
    #draw everything
    screen.fill(screen_color)
    pygame.draw.rect(screen,player_color,player)
    pygame.draw.rect(screen,goal_color,goalrect)
    for wall in walls:
        pygame.draw.rect(screen,wall_color,wall)
    for coin in coins:
        pygame.draw.rect(screen,coin_color,coin)
    for obstocle in obstocles:
        pygame.draw.rect(screen,ob_collor,(obstocle[0],obstocle[1],obstocle[2],obstocle[3]))
    #show the vin message
    if vin:
        vin_text=font.render("You win!",True,text_color)
        screen.blit(vin_text,(width//2-vin_text.get_width()//2,height//2))

        if pygame.time.get_ticks()-messagetimetime>=2000:
            running =False
    if game_over:
        messagetext=font.render("You lose!",True,text_color)
        screen.blit(messagetext,(width//2-vin_text.get_width()//2,height//2))

        if pygame.time.get_ticks()-messagetime>=2000:
            running =False
    pygame.display.update()
    clock.tick(20)


pygame.quit()
