import pygame
import random

pygame.init()


pygame.mixer.init()
engine_sound = pygame.mixer.Sound("car_accleration.mp3")
crash= pygame.mixer.Sound("crash.mp3")
# Screen dimensions
height = 750
width = 600
screen_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Road Race")
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
font_name = pygame.font.match_font("Times")

# Enemy car images
enemy_cars = [
    pygame.image.load("enemy_car.png"),
    pygame.image.load("3.png"),
    pygame.image.load("5.png"),
    pygame.image.load("enemy_car.png"),
    pygame.image.load("6.png")
]

# Function to draw text
def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# Player car class
class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("car.png").convert()
        self.image = pygame.transform.scale(self.image1, (70, 120))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 20
        self.speedx = 0

    def update(self):
        self.speedx = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.speedx = -12
            engine_sound.play()

        if key[pygame.K_d]:
            self.speedx = 12
            engine_sound.play() 

        self.rect.x += self.speedx
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0

# Enemy car class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = random.choice(enemy_cars) 
        self.image = pygame.transform.scale(self.image1, (70, 120))
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, width - self.rect.width)
        self.rect.y = random.randrange(-200, -40)
        self.speedy = random.randrange(2, 8)
    
    def update(self):
        global score
        self.rect.y += self.speedy
        # Reset the enemy position if it goes off the screen and increment the score
        if self.rect.top > height:
            self.rect.x = random.randrange(20, width - self.rect.width)
            self.rect.y = random.randrange(-150, -40)
            self.speedy = random.randrange(12, 17)
            score += 1  # Increment score when enemy passes the bottom

# Background
background1 = pygame.image.load("racetrack.png").convert_alpha()
background = pygame.transform.scale(background1, (600, 750))
bgrect = background.get_rect()

# Sprite groups
allsprite = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create player and enemies
player = Car()
allsprite.add(player)

for i in range(3):
    enemy = Enemy()
    allsprite.add(enemy)
    enemies.add(enemy)

# Game variables
running = True
game_over = False
score = 0  # Initialize score

# Game loop
while running:
    clock.tick(40)
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    allsprite.update()

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, enemies, False, pygame.sprite.collide_rect)
    if hits:
        crash.play()
        game_over = True


    # Draw everything
    screen_display.fill(black)
    screen_display.blit(background, bgrect)
    allsprite.draw(screen_display)

    # Draw the score at the top-left corner
    draw_text(screen_display, f"Score: {score}", 30, 30, 10)

    # Display game over message
    if game_over:
        draw_text(screen_display, "You lost", 50, width // 2, height // 2)
        pygame.display.update()
        pygame.time.wait(2000)
        running = False

    pygame.display.update()

pygame.quit()