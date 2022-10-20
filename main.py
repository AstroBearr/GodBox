import pygame,sys

pygame.init()
screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    screen.fill((0, 0, 0))

    pygame.display.update()

    clock.tick(60)
