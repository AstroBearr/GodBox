import pygame,sys
import random
import math

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)




class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,type = "water",temperature = 0):
        super().__init__()
        self.type = type
        self.temperature = random.randint(-5,5)
        self.image = pygame.surface.Surface((15,15))
        self.getColor()


        self.rect = self.image.get_rect(topleft=(x * 15,y * 15))

    def getColor(self):
        color = (0,0,0)
        if self.type == "water":
            color = (30,30,150)
        elif self.type == "grass":
            color = (30,150,30)
        elif self.type == "stone":
            color = (55,55,55)#Grey

        lst = list(color)
        lst[0] = clamp(lst[0] + self.temperature,0,255)
        lst[2] = clamp(lst[2] - self.temperature,0,255)
        color = tuple(lst)

        self.image.fill(color)

    def update(self):
        global selected
        if self.rect.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
            if(pygame.mouse.get_pressed(3)[0]):
                if selected >= 0:
                    self.type = "grass"
                if selected >= 2:
                    self.type = "stone"
                if selected >= 4:
                    self.type = "water"

                self.getColor()




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
        killsurf2 = gamefont2.render(f"", True, (0, 0, 0))
        killrect2 = killsurf2.get_rect(center=(600, 650))
        killsurf3 = gamefont2.render(f"stone", True, (0, 0, 0))
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
tiles = pygame.sprite.Group()
selected = 0
selectedstr = "grass"
pygame.mouse.set_visible(False)
for x in range(50):
    for y in range(50):
        tiles.add(Tile(x,y))
pygame.display.set_caption("God Box Beta")


while True:
    key = pygame.key.get_pressed()
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

    tiles.update()

    renderFont()

    screen.blit(pygame.image.load("Assets/Art/Mouse.png"), (pygame.mouse.get_pos()[0] - 10, pygame.mouse.get_pos()[1] - 4))

    pygame.display.update()

    if selected > 4:
        selected = 4
    if selected < 0:
        selected = 0

    clock.tick(60)
