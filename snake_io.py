import pygame
import random

pygame.init()

height=400
width=600
screen_color=(183,0,255)
screen_display=pygame.display.set_mode((width,height))

snake_color=(0,255,255)
food_color=(255,0,0)
font_color=(255,255,255)

block_size=20
font=pygame.font.SysFont("Arial Bold",30)
clock=pygame.time.Clock()

def draw_snake(block_size,snake_list):
    for x in snake_list:
        pygame.draw.rect(screen_display,snake_color,[x[0],x[1],block_size,block_size])
def message(messages,color):
    msg=font.render(messages,True,color)
    screen_display.blit(msg,[width//6,height//3])
def game_loop():
    game_over=False
    game_close=False
    #intial snake posittion
    x1=width//2
    y1=height//2
#intial movement direction
    x1change=0
    y1change=0

    snake_list=[]
    snake_lenght=1
    food_x= round(random.randrange(0,width-block_size)/block_size)*block_size
    food_y= round(random.randrange(0,height-block_size)/block_size)*block_size

    while not game_over:
        while game_close:
            screen_display.fill(screen_color)
            message("Your Loss!! Press Q to quit or R to Restart",font_color)
    
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_r:
                        game_loop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    x1change=-block_size
                    y1change=0
                if event.key==pygame.K_d:
                    x1change=block_size
                    y1change=0                   
                if event.key==pygame.K_w:
                    y1change=-block_size
                    x1change=0
                if event.key==pygame.K_s:
                    y1change=block_size
                    x1change=0
        if x1 >= width or x1<0 or y1 >= height or y1<0:
            game_close=True

        x1+=x1change#movement of snake 
        y1+=y1change#direction of snake
        screen_display.fill(screen_color)

        #draw food
        pygame.draw.rect(screen_display,food_color,[food_x,food_y,block_size,block_size])
        snakehead = []
        snakehead.append(x1)
        snakehead.append(y1)
        snake_list.append(snakehead)
        if len(snake_list)>snake_lenght:
            del snake_list[0]
        
        #check if the snake collideds with itself
            for x in snake_list[:-1]:
                if x == snakehead:
                    game_close=True

        draw_snake(block_size,snake_list)
        pygame.display.update()
        if x1==food_x and y1 == food_y:
            food_x= round(random.randrange(0,width-block_size)/block_size)*block_size
            food_y= round(random.randrange(0,height-block_size)/block_size)*block_size
            snake_lenght+=1
        clock.tick(10)
    pygame.quit()

game_loop()