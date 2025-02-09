import pygame

pygame.init()

name=pygame.display.set_mode((500,500))
pygame.display.set_caption("I Don't Know what to Put")

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
pygame.quit()
