import pygame,sys
import pygame

pygame.init()

# screen resolution
res = (720, 720)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (0, 0, 0)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()
green = (0, 255, 0)
red = (255, 0, 0)
# defining a font
click = False
smallfont = pygame.font.SysFont('Impact', 175, red)

# rendering a text written in
# this font
text = smallfont.render('START', True, color)
FirstScreen = True
SecondScreen = False
while FirstScreen:
    import pygame

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            FirstScreen = False
            SecondScreen = True

    smallfont = pygame.font.SysFont('Impact', 175,)
    green = (0, 255, 0)
    res = (720, 720)
    text = smallfont.render('START', True, color)
    width = screen.get_width()
    # stores the height of the
    color = (0, 0, 0)

    # light shade of the button
    color_light = (170, 170, 170)

    # dark shade of the button
    color_dark = (100, 100, 100)
    # screen into a variable
    height = screen.get_height()
    screen = pygame.display.set_mode(res)
    screen.fill((green))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])


    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

        # superimposing the text onto our button
        screen.blit(text, (40,35))

    # updates the frames of the game
        pygame.display.update()



class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y,type = "water"):
        super().__init__()
        self.type = type
        self.image = pygame.surface.Surface((15,15))
        if self.type == "water":
            self.image.fill("blue")
        elif self.type == "grass":
            self.image.fill("green")
        elif self.type == "stone":
            self.image.fill((55,55,55))#Grey

        self.rect = self.image.get_rect(topleft=(x * 15,y * 15))

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

                if self.type == "water":
                    self.image.fill("blue")
                elif self.type == "grass":
                    self.image.fill("green")
                elif self.type == "stone":
                    self.image.fill((55,55,55))#Grey




screen = pygame.display.set_mode((750, 750))
clock = pygame.time.Clock()
tiles = pygame.sprite.Group()
selected = 0
pygame.mouse.set_visible(False)
for x in range(50):
    for y in range(50):
        tiles.add(Tile(x,y))
pygame.display.set_caption("God Box Beta")


while SecondScreen:
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
