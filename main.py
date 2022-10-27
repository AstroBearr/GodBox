import pygame,sys

class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,type = "water"):
        super().__init__()
        self.type = type
        self.image = pygame.surface.Surface((5,5))
        if self.type == "water":
            self.image.fill("blue")
        elif self.type == "grass":
            self.image.fill("green")

        self.rect = self.image.get_rect(topleft=(x * 5,y * 5))

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
            if(pygame.mouse.get_pressed(3)[0]):
                self.type = "grass"


        if self.type == "water":
            self.image.fill("blue")
        elif self.type == "grass":
            self.image.fill("green")


pygame.init()
screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()
tiles = pygame.sprite.Group()
for x in range(150):
    for y in range(150):
        tiles.add(Tile(x,y))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    screen.fill((200, 200, 200))

    tiles.draw(screen)

    tiles.update()

    pygame.display.update()

    clock.tick(60)
