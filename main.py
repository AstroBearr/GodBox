import pygame,sys

ocean_0 = pygame.image.load("Assets/Art/pixil_ocean.png")
ocean_1 = pygame.image.load("Assets/Art/pixil_ocean2.png")

class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,type = "water"):
        super().__init__()
        self.type = type
        self.image = pygame.surface.Surface((15,15))
        if self.type == "water":
            self.image = pygame.image.load("Assets/Art/pixil_ocean.png")
        elif self.type == "grass":
            self.image.fill("green")
        elif self.type == "stone":
            self.image = pygame.image.load("Assets/Art/stone.png")

        self.rect = self.image.get_rect(topleft=(x * 15,y * 15))

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
            if(pygame.mouse.get_pressed(3)[0]):
                self.type = "grass"

                if self.type == "water":
                    self.image = pygame.image.load("Assets/Art/pixil_ocean.png")
                elif self.type == "grass":
                    self.image.fill("green")
                elif self.type == "stone":
                    self.image = pygame.image.load("Assets/Art/stone.png")



pygame.init()
screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()
tiles = pygame.sprite.Group()
pygame.mouse.set_visible(False)
for x in range(50):
    for y in range(50):
        tiles.add(Tile(x,y))
pygame.display.set_caption("God Box Beta")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    screen.fill((200, 200, 200))

    tiles.draw(screen)

    tiles.update()

    screen.blit(pygame.image.load("Assets/Art/Mouse.png"), (pygame.mouse.get_pos()[0] - 10, pygame.mouse.get_pos()[1] - 4))

    pygame.display.update()

    clock.tick(60)
