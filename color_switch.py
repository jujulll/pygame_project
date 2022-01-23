import pygame

size = width, height = 500, 700
pygame.init()
pygame.display.set_caption("CoLoR SwItCh")

screen = pygame.display.set_mode(size)

screen.fill((0, 0, 0))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
pygame.quit()