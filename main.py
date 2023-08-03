import pygame
import math
import random
from pygame import mixer
pygame.init()
# Display shits
ribbon = pygame.image.load("scoree.png")
ribbon = pygame.transform.scale(ribbon, (270, 239))
ribbont = pygame.transform.scale(ribbon, (260, 239))

# background music

mixer.music.load("music.wav")
mixer.music.play(-1)



def rib(x, y):
    screen.blit(ribbon, (x, y))


def ribt(x, y):
    screen.blit(ribbont, (x, y))


# screen
width = 1100
height = 800
screen = pygame.display.set_mode((width, height))
surface = pygame.Surface((width, height), pygame.SRCALPHA)
pygame.display.set_caption("Go Cinnamoroll Go!")

iconp = pygame.image.load("Cinnamoroll.png")
iconp = pygame.transform.scale(iconp, (32, 32))
pygame.display.set_icon(iconp)

# Background
bg = pygame.image.load("bg.png").convert_alpha()

# loading all images


# EXTRA
up = 0
up1 = 0
current_time = 0
pstop = 0
ostop = 0
life = 0
is_dead = False

# life
life_img = pygame.image.load("remaining.png").convert_alpha()
life1 = 255
life2 = 255
life3 = 255


def life_screen(x, y, z):
    life_img.set_alpha(z)
    screen.blit(life_img, (x, y))


# Score
score_value = 0
scorex = 905
scorey = 20

clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 36)
clockx = 40
clocky = 20


def score(x, y):
    score = font.render("Score: " + str(score_value), True, (190, 87, 0))
    screen.blit(score, (x, y))


# Player
pimg = pygame.image.load("icony1.png").convert_alpha()
pimg = pygame.transform.scale(pimg, (110, 110))
pX = 485
pY = 650
pXC = 0
pYC = 0


def player(x, y):
    screen.blit(pimg, (x, y))


# Objective1
cin = pygame.image.load("cinnamo.png")
o1x = 10
o1y = -150
o1yc = 4

# Objective2
o2x = 10
o2y = -150
o2yc = 4


def objective(x, y):
    screen.blit(cin, (x, y))


def reset():
    global pX
    global pY
    global score_value
    global up
    global up1
    global pXC
    global o1y
    global o1yc
    global o1yx
    global life
    global life1
    global life2
    global life3
    global is_dead

    pX = 485
    pY = 650
    score_value = 0
    up = 0
    up1 = 0
    pXC = 0
    o1y = -150
    o1yx = random.randint(0, 925)
    life = 0
    life1 = 255
    life2 = 255
    life3 = 255
    is_dead = False


# defining the Death screen

death = pygame.image.load("gg.png")


def deathscreen():
    global pX
    global pY
    global score_value
    global up
    global up1
    global pXC
    global o1y
    global o1yc
    global o1x
    global life
    global life1
    global life2
    global life3

    pX = 485
    pY = 650

    up = 0
    up1 = 0
    pXC = 0
    o1y = -150
    o1x = random.randint(0, 925)
    life1 = 0
    life2 = 0
    life3 = 0


    screen.blit(death, (360, 150))


# Collision
def collision(pX, pY, o1x, o1y):
    distance = math.sqrt((math.pow(pX - o1x, 2)) + (math.pow(pY - o1y, 2)))
    if distance <= 120:
        return True
    else:
        return False


def pause():
    global up1
    global o1yc
    global pXC
    global pstop
    global ostop

    pstop = pXC
    ostop = o1yc + up1


def resume():
    global pstop
    global ostop

    pstop = 0
    ostop = 0


pause()
# Loop for screen
running = True
while running:
    screen.fill((40, 208, 245))
    screen.blit(surface, (0, 0))
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # events in the game

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                reset()

            if event.key == pygame.K_LEFT:
                resume()
                pXC = -5 - int(up)

            if event.key == pygame.K_RIGHT:
                resume()
                pXC = 5 + int(up)
            if event.key == pygame.K_p:
                pause()
            if event.key == pygame.K_r:
                resume()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pXC = -5 - int(up)
                resume()
            if event.key == pygame.K_RIGHT:
                pXC = 5 + int(up)
                resume()
            if event.key == pygame.K_UP:
                reset()

            if event.key == pygame.K_p:
                pause()
            if event.key == pygame.K_r:
                resume()

    # making player move

    o1y = o1y + o1yc + up1 - ostop
    pX = pX + pXC - pstop
    if pX < -5:
        is_dead = True

    if pX >= 1005:
        is_dead = True

    if o1y >= 750:
        life = life + 1
        o1y = -150
        o1x = random.randint(0, 925)

    if life >= 3:
        is_dead = True

        # collision check

    col = collision(pX, pY, o1x, o1y)

    if col:
        score_value = score_value + 1
        up = up + 0.15
        up1 = up1 + 0.1
        cinnamo_sound = mixer.Sound("cinnamo_happy.wav")
        cinnamo_sound.play()

        o1y = -150
        o1x = random.randint(5, 920)

    if up >= 12:
        up = 12
    if up1 >= 9:
        up1 = 9

    if life == 1:
        life3 = 0

    if life == 2:
        life2 = 0

    if life == 3:
        life1 = 0

    if is_dead:
        deathscreen()

    ribt(-10, -80)
    life_screen(75, -30, life2)
    life_screen(20, -30, life1)
    life_screen(130, -30, life3)
    rib(845, -79)
    # time(clockx, clocky)
    score(scorex, scorey)
    player(pX, pY)
    objective(o1x, o1y)
    clock.tick(60)
    pygame.display.update()
