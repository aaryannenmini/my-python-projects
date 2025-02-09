import pygame

pygame.init()

WIDTH,HEIGHT=800,600

screen_display=pygame.display.set_mode(WIDTH,HEIGHT)
pygame.display.set_caption("Ping Pong")

WHITE=(255,255,255)
BLACK=(0,0,0)
R_PADDLE_COLOR=(0,0,255)
L_PADDLE_COLOR=(255,0,0)

PADDLE_WIDTH,PADDLE_HEIGHT = 20, 100
B_RADIUS=15

l_paddle_x = 30
r_paddle_x = WIDTH-30-PADDLE_WIDTH
l_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT //2
r_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT //2 
paddle_speed = 5

b_x=WIDTH//2
b_y=HEIGHT//2
b_speed_x = 5
b_speed_y = 5

l_score= 0
r_score=0
font=pygame.font.SysFont("Arial",30)

def draw_game():
    screen_display.fill(BLACK)

    pygame.draw.rect(screen_display,L_PADDLE_COLOR,(l_paddle_x,l_paddle_y,PADDLE_WIDTH,PADDLE_HEIGHT))
    pygame.draw.rect(screen_display,R_PADDLE_COLOR,(r_paddle_x,r_paddle_y,PADDLE_WIDTH,PADDLE_HEIGHT))

    pygame.draw.circle(screen_display,WHITE,(b_x,b_y),B_RADIUS)

    l_score_text=font.render(str(l_score),True,WHITE)
    screen_display.blit(l_score_text,(WIDTH//4-l_score_text.get_width()//2,20))

    r_score_text=font.render(str(r_score),True,WHITE)
    screen_display.blit(r_score_text,(WIDTH//4-r_score_text.get_width()//2,20))

def dotted_line():
    line_lenght=15
    line_gap=10
    center_x=WIDTH//2
    start_y=0
    end_y=HEIGHT

    y=start_y
    while y < end_y:
        pygame.draw.line(screen_display,WHITE,(center_x,y),(center_x,y+line_lenght))
        y+= line_lenght+ line_gap

def move_paddle():
    global l_paddle_y, r_paddle_y

    key=pygame.key.get_pressed()

    if key[pygame.K_w] and l_paddle_y > 0:
        l_paddle_y -= paddle_speed
    
    if key[pygame.K_w] and l_paddle_y < HEIGHT - PADDLE_HEIGHT:
        l_paddle_y += paddle_speed


    