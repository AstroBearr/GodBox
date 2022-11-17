import pygame,sys
import random
import math

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,type = "water",temperature = 0):
        super().__init__()
        self.type = type
        self.prev = type
        self.temperature = random.randint(-5, 5)
        self.image = pygame.surface.Surface((15,15))
        self.getColor()


        self.rect = self.image.get_rect(topleft=(x * 15,y * 15))

    def getColor(self):
        color = (0, 0, 0)
        if self.type == "water":
            color = (30, 30, 150)
        elif self.type == "grass":
            color = (30, 150, 30)
        elif self.type == "stone":
            color = (55, 55, 55)  # Grey

        lst = list(color)
        lst[0] = clamp(lst[0] + self.temperature, 0, 255)
        lst[2] = clamp(lst[2] - self.temperature, 0, 255)
        color = tuple(lst)

        self.image.fill(color)

    def update(self):
        global selected
        self.prev = self.type
        if self.rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
            if(pygame.mouse.get_pressed(3)[0]):
                if selected >= 0:
                    self.type = "grass"
                if selected >= 2:
                    self.type = "stone"
                if selected >= 4:
                    self.type = "water"
                if selected >= 6:
                    self.type = self.prev

                self.getColor()


class Human(pygame.sprite.Sprite):
    def __init__(self,x,y,generation=0,stats=[]):
        super().__init__()
        self.stats = stats
        self.gen = generation
        self.targetpos = [x,y]
        self.inwater = False
        self.image = pygame.image.load("Assets/Art/human_0.png")
        self.rect = self.image.get_rect(topleft=(x,y))
    def update(self):
        if self.inwater == False:
            if self.targetpos[0] > self.rect.x:
                self.rect.x += 1
            elif self.targetpos[0] < self.rect.x:
                self.rect.x -= 1
            if self.targetpos[1] > self.rect.y:
                self.rect.y += 1
            elif self.targetpos[1] < self.rect.y:
                self.rect.y -= 1
        if self.inwater == True:
            if self.targetpos[0] > self.rect.x:
                self.rect.x += 1
            elif self.targetpos[0] < self.rect.x:
                self.rect.x -= 1
            if self.targetpos[1] > self.rect.y:
                self.rect.y += 1
            elif self.targetpos[1] < self.rect.y:
                self.rect.y -= 1

        if random.randint(1, 100) == 69:
            self.targetpos = [self.rect.x + random.randint(-60,60), self.rect.y + random.randint(-60,60)]



def renderFont():
    global selectedstr
    killsurf2 = gamefont2.render(f"", True, (0, 0, 0))
    killrect2 = killsurf2.get_rect(center=(600, 650))
    killsurf3 = gamefont2.render(f"", True, (0, 0, 0))
    killrect3 = killsurf2.get_rect(center=(600 - 225, 650))
    if selected >= 0:
        selectedstr = "grass"
        killsurf2 = gamefont2.render(f"stone", True, (0, 0, 0))
        killrect2 = killsurf2.get_rect(center=(600, 650))
        killsurf3 = gamefont2.render(f"", True, (0, 0, 0))
        killrect3 = killsurf2.get_rect(center=(375 - 225, 650))
    if selected >= 2:
        selectedstr = "stone"
        killsurf2 = gamefont2.render(f"water", True, (0, 0, 0))
        killrect2 = killsurf2.get_rect(center=(600, 650))
        killsurf3 = gamefont2.render(f"grass", True, (0, 0, 0))
        killrect3 = killsurf2.get_rect(center=(375 - 225, 650))
    if selected >= 4:
        selectedstr = "water"
        killsurf2 = gamefont2.render(f"human", True, (0, 0, 0))
        killrect2 = killsurf2.get_rect(center=(600, 650))
        killsurf3 = gamefont2.render(f"stone", True, (0, 0, 0))
        killrect3 = killsurf2.get_rect(center=(375 - 225, 650))
    if selected >= 6:
        selectedstr = "human"
        killsurf2 = gamefont2.render(f"", True, (0, 0, 0))
        killrect2 = killsurf2.get_rect(center=(600, 650))
        killsurf3 = gamefont2.render(f"water", True, (0, 0, 0))
        killrect3 = killsurf2.get_rect(center=(375 - 225, 650))

    screen.blit(killsurf2, killrect2)
    screen.blit(killsurf3, killrect3)

    killsurf = gamefont.render(f"{selectedstr}", True, (0, 0, 0))
    killrect = killsurf.get_rect(center=(375, 650))
    screen.blit(killsurf, killrect)


pygame.init()
gamefont = pygame.font.Font('Assets/Fonts/blocco.ttf', 40)
gamefont2 = pygame.font.Font('Assets/Fonts/blocco.ttf', 15)
screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()
canmousedown = True
tiles = pygame.sprite.Group()
entities = pygame.sprite.Group()
selected = 0
selectedstr = "grass"
pygame.mouse.set_visible(False)
for x in range(50):
    for y in range(50):
        tiles.add(Tile(x,y))
pygame.display.set_caption("God Box Beta")


while True:
    for tile in tiles:
        for human in entities:
            if human.__class__ == Human:
                if human.rect.colliderect(tile.rect):
                    if tile.type == "water":
                        human.image = pygame.image.load("Assets/Art/human_0_swim.png")
                    else:
                        human.image = pygame.image.load("Assets/Art/human_0.png")


    key = pygame.key.get_pressed()
    if pygame.mouse.get_pressed(3)[0]:
        if(canmousedown):
            if selected >= 6:
                entities.add(Human(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], stats=[]))
                canmousedown = False
    else: canmousedown = True


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                selected += 1
            elif event.y == -1:
                selected -= 1
        if event.type == pygame.KEYUP:
            if key[pygame.K_RIGHT]:
                selected += 2
            if key[pygame.K_LEFT]:
                selected -= 2

    screen.fill("grey")

    tiles.draw(screen)

    entities.draw(screen)

    tiles.update()

    entities.update()

    renderFont()

    screen.blit(pygame.image.load("Assets/Art/Mouse.png"), (pygame.mouse.get_pos()[0] - 10, pygame.mouse.get_pos()[1] - 4))

    pygame.display.update()

    if selected > 6:
        selected = 6
    if selected < 0:
        selected = 0

    clock.tick(60)