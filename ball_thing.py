import pygame
import time
import random

pygame.init()

height = 700
width = 800
screen_color = (255, 0, 255)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Brick Game")

p_w = 100
p_h = 40
p_x = (width - p_w) // 2
p_y = (height - p_h - 30)
p_color = (255, 215, 0)
p_speed = 20

b_r = 20
b_color = (46, 46, 46)
b_x = width // 2
b_y = height // 2
bx_speed = 4
by_speed = -4

ob_r = 15
ob_color = (255, 69, 0)
ob_x = random.randint(ob_r, width - ob_r)
ob_y = random.randint(ob_r, height - ob_r)
obx_speed = 3
oby_speed = 3

s_w = 60
s_h = 20
BRICK_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]
stones = []

for i in range(5):
    for j in range(10):
        s_x = j * (s_w + 10) + 35
        s_y = i * (s_h + 5) + 40
        color = random.choice(BRICK_COLORS)  # Assign random color
        stones.append((pygame.Rect(s_x, s_y, s_w, s_h), color))

running = True
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans", 30)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and p_x < width - p_w:
        p_x += p_speed
    if keys[pygame.K_a] and p_x > 0:
        p_x -= p_speed

    b_x += bx_speed
    b_y += by_speed

    if b_x <= 0 or b_x >= width - b_r:
        bx_speed = -bx_speed
    if b_y <= 0:
        by_speed = -by_speed

    ob_x += obx_speed
    ob_y += oby_speed

    if ob_x <= 0 or ob_x >= width - ob_r:
        obx_speed = -obx_speed
    if ob_y <= 0 or ob_y >= height - ob_r:
        oby_speed = -oby_speed

    paddlerect = pygame.Rect(p_x, p_y, p_w, p_h)
    ballrect = pygame.Rect(b_x - b_r, b_y - b_r, b_r * 2, b_r * 2)

    if ballrect.colliderect(paddlerect):
        by_speed = -by_speed

    ob_ballrect = pygame.Rect(ob_x - ob_r, ob_y - ob_r, ob_r * 2, ob_r * 2)
    if ob_ballrect.colliderect(paddlerect):
        running = False
        message = "Game Over! You lost by hitting the obstacle ball."
        break

    for stone, color in stones[:]:  
        if ballrect.colliderect(stone):
            score += 100
            by_speed = -by_speed
            stones.remove((stone, color))

    if b_y >= height:
        running = False
        message = f"Game Over! Your Final Score is: {score}"
        break

    if not stones:
        running = False
        message = f"You Won! Your Final Score is: {score}"
        break

    screen.fill(screen_color)
    pygame.draw.rect(screen, p_color, paddlerect)
    pygame.draw.circle(screen, b_color, (b_x, b_y), b_r)
    pygame.draw.circle(screen, ob_color, (ob_x, ob_y), ob_r)  
    for stone, color in stones:
        pygame.draw.rect(screen, color, stone)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()
    clock.tick(60)

time.sleep(2)
screen.fill(screen_color)
message_text = font.render(message, True, (255, 255, 255))
screen.blit(message_text, (width // 2 - message_text.get_width() // 2, height // 2))
pygame.display.update()
time.sleep(2)
pygame.quit()
