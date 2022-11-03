import pygame,sys

class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,type = "water",temperature = 0):
        super().__init__()
        self.type = type
        self.temperature = temperature
        self.image = pygame.surface.Surface((15,15))
        self.getColor()


        self.rect = self.image.get_rect(topleft=(x * 15,y * 15))

    def getColor(self):
        if self.type == "water":
            self.image.fill("blue")
        elif self.type == "grass":
            self.image.fill("green")
        elif self.type == "stone":
            self.image.fill((55,55,55))#Grey

    def update(self):
        global selected
        if self.rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
            if(pygame.mouse.get_pressed(3)[0]):
                if selected >= 0:
                    self.type = "grass"
                if selected >= 4:
                    self.type = "stone"
                if selected >= 8:
                    self.type = "water"

                self.getColor()



pygame.init()
screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()
tiles = pygame.sprite.Group()
selected = 0
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
        elif event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                selected += 1
            elif event.y == -1:
                selected -= 1


    screen.fill((200, 200, 200))

    tiles.draw(screen)

    tiles.update()

    screen.blit(pygame.image.load("Assets/Art/Mouse.png"), (pygame.mouse.get_pos()[0] - 10, pygame.mouse.get_pos()[1] - 4))

    pygame.display.update()

    if selected > 8:
        selected = 8

    clock.tick(60)
