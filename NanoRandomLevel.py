import pygame
import sys
import random as rd
import time
from pygame import mixer, font
import pickle
from pygame.locals import *

# INITIALIZE PYGAME
pygame.init()
pygame.font.init()
# SCREEN SIZE
clock = pygame.time.Clock()
fps = 60
screenWidth = 852
screenHeight = screenWidth

# LEVI IMAGES INITIALIZATION
WalkRight = [pygame.image.load('img/R1.png'), pygame.image.load('img/R2.png'), pygame.image.load('img/R3.png'),
             pygame.image.load('img/R4.png'), pygame.image.load('img/R5.png'), pygame.image.load('img/R6.png'),
             pygame.image.load('img/R7.png'), pygame.image.load('img/R8.png'), pygame.image.load('img/R9.png')]
WalkRUp = [pygame.image.load('img/RU1.png'), pygame.image.load('img/RU2.png'), pygame.image.load('img/RU3.png'),
           pygame.image.load('img/RU4.png'), pygame.image.load('img/RU5.png'), pygame.image.load('img/RU6.png'),
           pygame.image.load('img/RU7.png'), pygame.image.load('img/RU8.png'), pygame.image.load('img/RU9.png')]
WalkLUp = [pygame.image.load('img/LU1.png'), pygame.image.load('img/LU2.png'), pygame.image.load('img/LU3.png'),
           pygame.image.load('img/LU4.png'), pygame.image.load('img/LU5.png'), pygame.image.load('img/LU6.png'),
           pygame.image.load('img/LU7.png'), pygame.image.load('img/LU8.png'), pygame.image.load('img/LU9.png')]
WalkLeft = [pygame.image.load('img/L1.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'),
            pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'),
            pygame.image.load('img/L7.png'), pygame.image.load('img/L8.png'), pygame.image.load('img/L9.png')]
WalkLeftDown = [pygame.image.load('img/DL1.png'), pygame.image.load('img/DL2.png'), pygame.image.load('img/DL3.png'),
                pygame.image.load('img/DL4.png'), pygame.image.load('img/DL5.png'), pygame.image.load('img/DL6.png'),
                pygame.image.load('img/DL7.png'), pygame.image.load('img/DL8.png'), pygame.image.load('img/DL9.png')]
WalkRightDown = [pygame.image.load('img/DR1.png'), pygame.image.load('img/DR2.png'), pygame.image.load('img/DR3.png'),
                 pygame.image.load('img/DR4.png'), pygame.image.load('img/DR5.png'), pygame.image.load('img/DR6.png'),
                 pygame.image.load('img/DR7.png'), pygame.image.load('img/DR8.png'), pygame.image.load('img/DR9.png')]
SpinExit = [pygame.image.load('img/Spin1.png'), pygame.image.load('img/Spin2.png'), pygame.image.load('img/Spin3.png'),
            pygame.image.load('img/Spin4.png'), pygame.image.load('img/Spin5.png'), pygame.image.load('img/Spin6.png'),
            pygame.image.load('img/Spin7.png'), pygame.image.load('img/Spin8.png'), pygame.image.load('img/Spin9.png')]
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Nano World")

width = (screenWidth // 10) - 2  # size of the side of box
height = (screenHeight // 10) - 2  # size of the side of box
movement = (screenHeight // 10)  # Each square is = 85

x = 1
y = 1

AlienX = x
AlienY = y
start_img = pygame.image.load('img/start_btn.png')
exit_img = pygame.image.load('img/exit_btn.png')
count = 0

# TEMP VALUE FOR X,Y FOR WINNING CONDITION
x += 1
y += 1

walkCount = 0
Goldx = (rd.randint(0, 9) * movement) + 1  # GOLD X COORDINATE
Goldy = (rd.randint(0, 9) * movement) + 1  # GOLD Y COORDINATE

NanoX = (rd.randint(1, 9) * movement) + 1  # NANO X COORDINATE
NanoY = (rd.randint(0, 9) * movement) + 1  # NANO Y COORDINATE

PitX = (rd.randint(1, 9) * movement) + 1  # PIT X COORDINATE
PitY = (rd.randint(0, 9) * movement) + 1  # PIT Y COORDINATE

coor1 = 2
coor2 = 2

RotateCount = 0  # 0 - LEFT, 1 - RIGHT, 2 - R.UP, 3 - L.UP, 4 - L.DOWN, 5 - R.DOWN
font = pygame.font.SysFont('Constantia', 30)
# COLORS & SOUND
bg = (204, 102, 0)
BLACK = (0, 0, 0)
GOLD = (255, 215, 0)
RED = (200, 0, 0)
GREEN = (0, 128, 0)
GREY = (128, 128, 128)
DGREY = (112, 128, 144)
theme = mixer.music.load('img/Soundtheme.wav')
mixer.music.play(-1)
sound = pygame.mixer.Sound('img/KENNY.wav')
sound2 = pygame.mixer.Sound('img/blow.wav')
sound3 = pygame.mixer.Sound('img/Fairy.wav')
scan = 0
background_image = pygame.image.load("img/home.png")
# BOOLEAN FOR ANIMATION
rUp = False
lUp = False
lDown = False
rDown = False
right = True
left = False
run = True
waiting = False
#Global
clicked = False
main_menu = True
game = False
counter = 0


class button():
    # colours for button and text
    button_col = (255, 0, 0)
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = BLACK
    width = width
    height = height

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):

        global clicked
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()

        # create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        # check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(win, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(win, self.hover_col, button_rect)
        else:
            pygame.draw.rect(win, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(win, BLACK, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(win, BLACK, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(win, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(win, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        win.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action


again = button(260, 200, 'Play')
quit = button(460, 200, 'Quit')

def CountSteps(choice, color, font, size):
    step_font = pygame.font.SysFont(font, size)
    step_surface = step_font.render('Steps:' + str(count), True, color)
    step_rect = step_surface.get_rect()
    if choice == 1:
        step_rect.midtop = (screenWidth / 6.7, screenHeight / 40)
    else:
        step_rect.midtop = (screenWidth / 2, screenHeight / 1.25)
    win.blit(step_surface, step_rect)

def CountScans(choice, color, font, size):
    step_font = pygame.font.SysFont(font, size)
    step_surface = step_font.render('Scans:' + str(scan), True, color)
    step_rect = step_surface.get_rect()
    if choice == 1:
        step_rect.midtop = (screenWidth / 20, screenHeight / 40)
    else:
        step_rect.midtop = (screenWidth / 2, screenHeight / 1.50)
    win.blit(step_surface, step_rect)


def Win():
    my_font = pygame.font.SysFont('times new roman', 60)
    winner_surface = my_font.render('SEARCH SUCCESSFUL!', True, GOLD)
    winner_rect = winner_surface.get_rect()
    winner_rect.midtop = (screenWidth / 2, screenHeight / 4)
    win.fill(BLACK)
    win.blit(winner_surface, winner_rect)
    CountSteps(0, GOLD, 'times new roman', 50)
    CountScans(0, GOLD, 'time new roman', 50)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def GameOver():
    my_font = pygame.font.SysFont('times new roman', 60)
    game_over_surface = my_font.render('SEARCH UNSUCCESSFUL!', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screenWidth / 2, screenHeight / 4)
    win.fill(BLACK)
    win.blit(game_over_surface, game_over_rect)
    CountSteps(0, RED, 'times new roman', 50)
    CountScans(0, RED, 'time new roman', 50)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def drawGrid():
    blockSize = (screenWidth // 10)  # Set the size of the grid block
    for x in range(0, screenWidth, blockSize):
        for y in range(0, screenHeight, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(win, BLACK, rect, 1)


# main loop
# main loop

while run:
    win.blit(background_image, [0, 0])

    if again.draw_button():
        game = True
    if quit.draw_button():
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

    while game:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        # FOR RANDOM MOVEMENT
        rdMove = 0
        rdAlienMove = 0
        rdAlienMove = rd.randint(0, 4)
        # MOVEMENT CONDITIONS
        if rdAlienMove == 1 and AlienX < screenWidth - width - movement:  # GO RIGHT
            RotateCount = 1
            rdMove = rd.randint(1, 4)
            AlienX += movement
            count += 1
            right = True
            left = False
            rUp = False
            lUp = False
            lDown = False
            rDown = False

        elif rdAlienMove == 2 and AlienX > movement:  # GO LEFT
            RotateCount = 0
            rdMove = rd.randint(1, 4)
            AlienX -= movement
            count += 1
            right = False
            left = True
            rUp = False
            lUp = False
            lDown = False
            rDown = False

        elif rdAlienMove == 3 and AlienY > movement:  # GO DOWN
            AlienY -= movement
            rdMove = rd.randint(1, 4)
            count += 1
            right = False
            left = False
            if RotateCount == 1:  # RIGHT SIDE UP
                rUp = True
                lUp = False
                RotateCount = 2
                scan += 1
            elif RotateCount == 0:  # LEFT SIDE UP
                rUp = False
                lUp = True
                RotateCount = 3
                scan += 1
            elif RotateCount == 4:  # RIGHT SIDE UP
                rUp = False
                lUp = True
                RotateCount = 3
                scan += 1
            elif RotateCount == 5:  # LEFT SIDE UP
                rUp = True
                lUp = False
                RotateCount = 2
                scan += 1


        elif rdAlienMove == 4 and AlienY < screenHeight - height - movement:
            AlienY += movement
            rdMove = rd.randint(1, 4)
            count += 1
            right = False
            left = False
            if RotateCount == 0:  # LEFT SIDE DOWN
                lDown = True
                rDown = False
                RotateCount = 4
            elif RotateCount == 1:  # RIGHT SIDE DOWN
                lDown = False
                rDown = True
                RotateCount = 5
            elif RotateCount == 2:  # RIGHT SIDE DOWN
                lDown = False
                rDown = True
                RotateCount = 5
            elif RotateCount == 3:  # LEFT SIDE DOWN
                lDown = True
                rDown = False
                RotateCount = 4

        else:  # STATIONARY POSITION
            if RotateCount == 1:  # LOOKING RIGHT
                right = True
                left = False
                rUp = False
                lUp = False
                lDown = False
                rDown = False
            elif RotateCount == 0:  # LOOKING LEFT
                left = True
                right = False
                rUp = False
                lUp = False
                lDown = False
                rDown = False
            elif RotateCount == 2:  # LOOKING RIGHT UP
                right = False
                left = False
                rUp = True
                lUp = False
                lDown = False
                rDown = False
            elif RotateCount == 3:  # LOOKING LEFT UP
                right = False
                left = False
                rUp = False
                lUp = True
                lDown = False
                rDown = False
            elif RotateCount == 4:  # LOOKING LEFT DOWN
                right = False
                left = False
                rUp = False
                lUp = False
                lDown = True
                rDown = False
            elif RotateCount == 5:  # LOOKING RIGHT DOWN
                right = False
                left = False
                rUp = False
                lUp = False
                lDown = False
                rDown = True

        # CONDITIONS
        if (AlienX == Goldx) and (AlienY == Goldy):  # GLITTERS FOR GOLD
            Goldx = screenHeight
            Goldy = screenWidth
            x = 1
            y = 1

        if (AlienX == PitX) and (AlienY == PitY):  # FELL DOWN PIT
            GameOver()
        if (AlienX == NanoX) and (AlienY == NanoY):  # EATEN BY NANO
            GameOver()
        if AlienX == x and AlienY == y:  # GOT THE GOLD, GOT BACK IN STARTING POS
            Win()

        # GOLD GLITTERS DISPLAY
        if (AlienX == Goldx + 85) and (AlienY == Goldy + 85) \
                or (AlienX == Goldx + 85) and (AlienY == Goldy - 85) \
                or (AlienX == Goldx - 85) and (AlienY == Goldy - 85) \
                or (AlienX == Goldx - 85) and (AlienY == Goldy + 85) \
                or (AlienX == Goldx + 85) and (AlienY == Goldy) \
                or (AlienX == Goldx - 85) and (AlienY == Goldy) \
                or (AlienX == Goldx) and (AlienY == Goldy + 85) \
                or (AlienX == Goldx) and (AlienY == Goldy - 85):
            pygame.draw.rect(win, GOLD, (Goldx + 85, Goldy + 85, width, height))
            pygame.draw.rect(win, GOLD, (Goldx + 85, Goldy - 85, width, height))
            pygame.draw.rect(win, GOLD, (Goldx - 85, Goldy - 85, width, height))
            pygame.draw.rect(win, GOLD, (Goldx - 85, Goldy + 85, width, height))
            pygame.draw.rect(win, GOLD, (Goldx + 85, Goldy, width, height))
            pygame.draw.rect(win, GOLD, (Goldx - 85, Goldy, width, height))
            pygame.draw.rect(win, GOLD, (Goldx, Goldy + 85, width, height))
            pygame.draw.rect(win, GOLD, (Goldx, Goldy - 85, width, height))
            pygame.display.update()
        # PIT BREEZE DISPLAY AND SOUND
        if (AlienX == PitX + 85 and AlienY == PitY + 85) \
                or (AlienX == PitX + 85 and AlienY == PitY - 85) \
                or (AlienX == PitX - 85 and AlienY == PitY - 85) \
                or (AlienX == PitX - 85 and AlienY == PitY + 85) \
                or (AlienX == PitX + 85 and AlienY == PitY) \
                or (AlienX == PitX - 85 and AlienY == PitY) \
                or (AlienX == PitX and AlienY == PitY + 85) \
                or (AlienX == PitX and AlienY == PitY - 85):
            sound2.play()
            pygame.draw.rect(win, DGREY, (PitX + 85, PitY + 85, width, height))
            pygame.draw.rect(win, DGREY, (PitX + 85, PitY - 85, width, height))
            pygame.draw.rect(win, DGREY, (PitX - 85, PitY - 85, width, height))
            pygame.draw.rect(win, DGREY, (PitX - 85, PitY + 85, width, height))

            pygame.draw.rect(win, DGREY, (PitX + 85, PitY, width, height))
            pygame.draw.rect(win, DGREY, (PitX - 85, PitY, width, height))
            pygame.draw.rect(win, DGREY, (PitX, PitY + 85, width, height))
            pygame.draw.rect(win, DGREY, (PitX, PitY - 85, width, height))
            pygame.display.update()

        # WHITE BACKGROUND FOR MAP
        win.fill((255, 255, 255))
        # NANO MOVEMENT 1
        if rdMove == 1:
            pygame.draw.rect(win, GREEN, (NanoX + 85, NanoY, width, height))
            pygame.draw.rect(win, GREEN, (NanoX - 85, NanoY, width, height))
            pygame.draw.rect(win, GREEN, (NanoX, NanoY + 85, width, height))
            pygame.draw.rect(win, (255, 192, 203), (NanoX, NanoY - 85, width, height))  # BACK SIDE IS NORTH
            if AlienX == NanoX and AlienY == NanoY - 85:  # BACKSIDE/CONDITION FOR ALIEN TO SHOOT NANO
                sound.play()
                NanoX = screenHeight
                NanoY = screenWidth
                # KILLING ANIMATION
                if walkCount + 1 >= 27:
                    walkCount = 0
                else:
                    win.blit(SpinExit[walkCount // 3], (AlienX, AlienY))
                    walkCount += 1
            # ALIEN LANDED IN FRONT OF NANO
            elif (AlienX == NanoX + 85 and AlienY == NanoY) \
                    or (AlienX == NanoX - 85 and AlienY == NanoY) \
                    or (AlienX == NanoX and AlienY == NanoY + 85):
                GameOver()
        # NANO MOVEMENT 2
        if rdMove == 2:
            pygame.draw.rect(win, GREEN, (NanoX + 85, NanoY, width, height))
            pygame.draw.rect(win, GREEN, (NanoX - 85, NanoY, width, height))
            pygame.draw.rect(win, (255, 192, 203), (NanoX, NanoY + 85, width, height))  # BACK SIDE IS SOUTH
            pygame.draw.rect(win, GREEN, (NanoX, NanoY - 85, width, height))
            if AlienX == NanoX and AlienY == NanoY + 85:  # BACKSIDE/CONDITION FOR ALIEN TO SHOOT NANO
                sound.play()
                NanoX = screenHeight
                NanoY = screenWidth
                # KILLING ANIMATION
                if walkCount + 1 >= 27:
                    walkCount = 0
                else:
                    win.blit(SpinExit[walkCount // 3], (AlienX, AlienY))
                    walkCount += 1
            # ALIEN LANDED IN FRONT OF NANO
            elif (AlienX == NanoX + 85 and AlienY == NanoY) \
                    or (AlienX == NanoX - 85 and AlienY == NanoY) \
                    or (AlienX == NanoX and AlienY == NanoY - 85):
                GameOver()
        # NANO MOVEMENT 3
        if rdMove == 3:
            pygame.draw.rect(win, GREEN, (NanoX + 85, NanoY, width, height))
            pygame.draw.rect(win, (255, 192, 203), (NanoX - 85, NanoY, width, height))  # BACK SIDE IS WEST
            pygame.draw.rect(win, GREEN, (NanoX, NanoY + 85, width, height))
            pygame.draw.rect(win, GREEN, (NanoX, NanoY - 85, width, height))
            if AlienX == NanoX - 85 and AlienY == NanoY:  # BACKSIDE/CONDITION FOR ALIEN TO SHOOT NANO
                sound.play()
                NanoX = screenHeight
                NanoY = screenWidth
                # KILLING ANIMATION
                if walkCount + 1 >= 27:
                    walkCount = 0
                else:
                    win.blit(SpinExit[walkCount // 3], (AlienX, AlienY))
                    walkCount += 1
            # ALIEN LANDED IN FRONT OF NANO
            elif (AlienX == NanoX + 85 and AlienY == NanoY) \
                    or (AlienX == NanoX and AlienY == NanoY + 85) \
                    or (AlienX == NanoX and AlienY == NanoY - 85):
                GameOver()
        # NANO MOVEMENT 4
        if rdMove == 4:
            pygame.draw.rect(win, (255, 192, 203), (NanoX + 85, NanoY, width, height))  # BACK SIDE IS EAST
            pygame.draw.rect(win, GREEN, (NanoX - 85, NanoY, width, height))
            pygame.draw.rect(win, GREEN, (NanoX, NanoY + 85, width, height))
            pygame.draw.rect(win, GREEN, (NanoX, NanoY - 85, width, height))
            if AlienX == NanoX + 85 and AlienY == NanoY:  # BACKSIDE/CONDITION FOR ALIEN TO SHOOT NANO
                sound.play()
                NanoX = screenHeight
                NanoY = screenWidth
                # KILLING AANIMATION
                if walkCount + 1 >= 27:
                    walkCount = 0
                else:
                    win.blit(SpinExit[walkCount // 3], (AlienX, AlienY))
                    walkCount += 1
            # ALIEN LANDED IN FRONT OF NANO
            elif (AlienX == NanoX - 85 and AlienY == NanoY) \
                    or (AlienX == NanoX and AlienY == NanoY + 85) \
                    or (AlienX == NanoX - 85 and AlienY == NanoY - 85):
                GameOver()

                # LEVI ANIMATION
        if walkCount + 1 >= 27:
            walkCount = 0
        if run and right:  # WALKING RIGHT
            win.blit(WalkRight[walkCount // 3], (AlienX, AlienY))
            walkCount += 1
        elif run and rUp:  # WALKING RIGHT UP
            win.blit(WalkRUp[walkCount // 3], (AlienX, AlienY))
            walkCount += 1
        elif run and left:  # WALKING LEFT
            win.blit(WalkLeft[walkCount // 3], (AlienX, AlienY))
            walkCount += 1
        elif run and lUp:  # WALKING LEFT UP
            win.blit(WalkLUp[walkCount // 3], (AlienX, AlienY))
            walkCount += 1
        elif run and lDown:  # WALKING LEFT DOWN
            win.blit(WalkLeftDown[walkCount // 3], (AlienX, AlienY))
            walkCount += 1
        elif run and rDown:  # WALKING RIGHT DOWN
            win.blit(WalkRightDown[walkCount // 3], (AlienX, AlienY))
            walkCount += 1
        else:  # EXITING GAME ANIMATION
            win.blit(SpinExit[walkCount // 3], (AlienX, AlienY))
            walkCount += 1

        pygame.draw.rect(win, GOLD, (Goldx, Goldy, width, height))  # DISPLAY GOLD
        pygame.draw.rect(win, GREEN, (NanoX, NanoY, width, height))  # DISPLAY NANO
        pygame.draw.rect(win, GREY, (PitX, PitY, width, height))  # DISPLAY PIT
        CountSteps(1, BLACK, 'monospace', 16)
        CountScans(1, BLACK, 'monospace', 16)
        drawGrid()
        pygame.display.update()




pygame.quit()
