import pygame
import random

pygame.init()
width = 800
height = 600
screen_color = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")

# Paddle variables
padc = (0, 20, 168)
padw = 100
padh = 20
padx = (width - padw) // 2
pady = (height - padh) - 20
pads = 20

# Green ball variables
br = 15  # Ball radius
bs = 10  # Ball speed
bx = random.randint(br, width - br)
by = random.randint(-height, -br)  # Random initial position above the screen
bc = (0, 255, 0)
bcount = 0

# Red ball variables
rbr = 15  # Red ball radius
rbs = 8  # Red ball speed
rbx = random.randint(rbr, width - rbr)
rby = random.randint(-height, -rbr)  # Random initial position above the screen
rbc = (255, 0, 0)

# Score
s = 0
f_equal_font = pygame.font.SysFont("Hobo", 50)
tc = (0, 0, 0)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()

    if key[pygame.K_d] and padx < width - padw:
        padx += pads
    if key[pygame.K_a] and padx > 0:
        padx -= pads

    # Green ball movement
    by += bs

    # Red ball movement
    rby += rbs

    # Reset green ball if it goes off-screen
    if by > height:
        bx = random.randint(br, width - br)
        by = random.randint(-height, -br)  # Reset to a random position above the screen
        bcount += 1

    # Reset red ball if it goes off-screen
    if rby > height:
        rbx = random.randint(rbr, width - rbr)
        rby = random.randint(-height, -rbr)  # Reset to a random position above the screen

    # Green ball collision with paddle
    if (padx < bx < padx + padw) and (pady < by + br < pady + padh):
        s += 10
        bx = random.randint(br, width - br)
        by = random.randint(-height, -br)  # Reset to a random position above the screen
        bcount += 1

    # Red ball collision with paddle
    if (padx < rbx < padx + padw) and (pady < rby + rbr < pady + padh):
        s -= 5
        rbx = random.randint(rbr, width - rbr)
        rby = random.randint(-height, -rbr)  # Reset to a random position above the screen

    # Fill screen color
    screen.fill(screen_color)

    # Draw paddle
    pygame.draw.rect(screen, padc, (padx, pady, padw, padh))

    # Draw green ball
    pygame.draw.circle(screen, bc, (bx, by), br)

    # Draw red ball
    pygame.draw.circle(screen, rbc, (rbx, rby), rbr)

    # Display score
    score_t = f_equal_font.render(f"Score: {s}", True, tc)
    screen.blit(score_t, (10, 10))

    # Display ball count
    btext = f_equal_font.render(f"Ball: {bcount}", True, tc)
    screen.blit(btext, (600, 10))

    pygame.display.update()
    clock.tick(120)

pygame.quit()
