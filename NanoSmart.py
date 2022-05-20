import pygame
from queue import PriorityQueue
import random as rd
import time
import sys
from pygame import mixer, font
from pygame.locals import *

pygame.init()
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Nano World")

walk = True
run = True
width = (WIDTH// 10) - 2
height = (WIDTH// 10) - 2
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 128, 0)
WHITE = (255, 255, 255)
DIRTYWHITE = (232, 228, 201)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
GOLD = (255, 215, 0)
DIRTY_YELLOW = (232, 228, 0)
bg = (204, 102, 0)

# LEVI IMAGES INITIALIZATION
LEVI = pygame.image.load('img/R4.png')
LEVI_l = pygame.image.load('img/L4.png')
background_image = pygame.image.load("img/home.png")
# count steps
count = 0
scan = 2
theme = mixer.music.load('img/Soundtheme.wav')
mixer.music.play(-1)
font = pygame.font.SysFont('time new roman', 30)

#Global
clicked = False
game = False

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
                pygame.draw.rect(WIN, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(WIN, self.hover_col, button_rect)
        else:
            pygame.draw.rect(WIN, self.button_col, button_rect)

        # add shading to button
        pygame.draw.line(WIN, BLACK, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(WIN, BLACK, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(WIN, BLACK, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(WIN, BLACK, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        # add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        WIN.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action


again = button(260, 200, 'Play')
quit = button(460, 200, 'Quit')

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.walkCount = 0
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

        self.alienX = 0
        self.alienY = 0

        self.Goldx = rd.randint(1, 9)  # GOLD X COORDINATE
        self.Goldy = rd.randint(0, 9)

        self.run = run

        self.PitX = rd.randint(1, 9)
        self.PitY = rd.randint(0, 9)

        self.NanoX = rd.randint(1, 9)
        self.NanoY = rd.randint(0, 9)

    def get_pos(self):
        return self.row, self.col

    def collisions(self):
        return self.color == GREY

    def collisions_Nano(self):
        return self.color == DARKGREEN

    def Alien_rep(self):
        self.color = GREEN
        WIN.blit(LEVI, (self.x, self.y))

    def is_visited(self):
        self.color = DIRTYWHITE

    def to_be_visited(self):
        self.color = ORANGE

    def is_Pit(self):
        self.color = GREY

    def is_Gold(self):
        self.color = GOLD

    def gold_taken(self):
        self.color = WHITE

    def is_Nano(self):
        self.color = DARKGREEN

    def shortest_path(self):
        WIN.blit(LEVI_l, (self.x, self.y))

    def shortest_path_pic(self):
        pass

    def draw(self, win):
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def draw_LEVI(self, win):
        # pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        win.blit(LEVI, (self.x, self.y))

    def update_neighbors(self, grid):  # FOR SMART MOVEMENT!!!
        self.neighbors = []
        # DOWN
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].collisions() and not grid[self.row + 1][
            self.col].collisions_Nano():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].collisions() and not grid[self.row - 1][
            self.col].collisions_Nano():  # UP
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].collisions() and not grid[self.row][
            self.col + 1].collisions_Nano():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].collisions() and not grid[self.row][
            self.col - 1].collisions_Nano():  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

        pygame.display.update()

    def __lt__(self, other):
        return False


def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_shortest_path(prev_path, current, draw):
    while current in prev_path:
        current = prev_path[current]
        pygame.time.delay(250)
        current.Alien_rep()
        global count
        count += 1
        pygame.display.update()
        draw()
    # pygame.display.update()


def a_star(draw, grid, start, end):
    count = 0
    prio_queue = PriorityQueue()
    prio_queue.put((0, count, start))
    prev_path = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = manhattan(start.get_pos(), end.get_pos())

    prio_queue_hash = {start}

    while not prio_queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = prio_queue.get()[2]
        prio_queue_hash.remove(current)

        if current == end:
            reconstruct_shortest_path(prev_path, end, draw)
            end.gold_taken()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                prev_path[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + \
                                    manhattan(neighbor.get_pos(), end.get_pos())
                if neighbor not in prio_queue_hash:
                    count += 1
                    prio_queue.put((f_score[neighbor], count, neighbor))
                    prio_queue_hash.add(neighbor)
                    # neighbor.to_be_visited()

        draw()
        pygame.display.update()

        if current != start:
            current.is_visited()

    return False


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw(win, grid, rows, width):
    win.fill(WHITE)
    global count
    for row in grid:
        for spot in row:
            spot.draw(win)

    gap = width // rows
    CountSteps(count, 1, BLACK, 'monospace', 15)
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))


def CountSteps(count, choice, color, font, size):
    step_font = pygame.font.SysFont(font, size)
    step_surface = step_font.render('Steps: ' + str(count), True, color)
    step_rect = step_surface.get_rect()
    if choice == 1:
        step_rect.midtop = (WIDTH / 20, WIDTH / 40)
    else:
        step_rect.midtop = (WIDTH / 2, WIDTH / 1.25)
    WIN.blit(step_surface, step_rect)


def CountScans(choice, color, font, size):
    step_font = pygame.font.SysFont(font, size)
    step_surface = step_font.render('Scans:' + str(scan), True, color)
    step_rect = step_surface.get_rect()
    if choice == 1:
        step_rect.midtop = (WIDTH / 20, WIDTH / 40)
    else:
        step_rect.midtop = (WIDTH / 2, WIDTH / 1.50)
    WIN.blit(step_surface, step_rect)


def Win():
    my_font = pygame.font.SysFont('times new roman', 90)
    winner_surface = my_font.render('SCANNED', True, GOLD)
    winner_rect = winner_surface.get_rect()
    winner_rect.midtop = (WIDTH / 2, WIDTH / 4)
    WIN.fill(BLACK)
    WIN.blit(winner_surface, winner_rect)
    CountScans(0, GOLD, 'time new roman', 50)
    CountSteps(count, 0, GOLD, 'time new roman', 50)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def No_path():
    my_font = pygame.font.SysFont('times new roman', 90)
    winner_surface = my_font.render('NO PATH MADE', True, RED)
    winner_rect = winner_surface.get_rect()
    winner_rect.midtop = (WIDTH / 2, WIDTH / 4)
    WIN.fill(BLACK)
    WIN.blit(winner_surface, winner_rect)
    CountScans(0, RED, 'time new roman', 50)
    CountSteps(count, 0, RED, 'time new roman', 50)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


def main(win, width):
    global game
    ROWS = 10
    grid = make_grid(ROWS, width)

    global count
    alienX = 0
    alienY = 0

    Goldx = rd.randint(1, 9)  # GOLD X COORDINATE
    Goldy = rd.randint(0, 9)

    PitX = rd.randint(1, 9)
    PitY = rd.randint(0, 9)

    NanoX = rd.randint(1, 9)
    NanoY = rd.randint(0, 9)


    run = True

    gold_taken = 0

    while run:

        WIN.blit(background_image, [0, 0])

        if again.draw_button():
            game = True
        if quit.draw_button():
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

        while game:
            draw(win, grid, ROWS, width)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                row, col = alienX, alienY
                A_Spot = grid[row][col]
                start = A_Spot
                start.Alien_rep()
                pygame.display.update()


                G_Spot = grid[Goldx][Goldy]
                end = G_Spot
                end.is_Gold()

                if (start == end):
                    end.gold_taken()

                # pit
                for x in range(5):
                    row = PitX
                    col = PitY
                    P_Spot = grid[x + 1][col - x]
                    P_Spot.is_Pit()

                # Nano
                row, col = NanoX, NanoY
                N_Spot = grid[row][col]
                N_Spot.is_Nano()

                # perform search
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and start and end:
                        for row in grid:
                            for spot in row:
                                spot.update_neighbors(grid)
                                pygame.display.update()
                        a_star(lambda: draw(win, grid, ROWS, width), grid, end, start)
                        gold_taken += 1
                        a_star(lambda: draw(win, grid, ROWS, width), grid, start, end)

                        pygame.display.update()
                        pygame.time.delay(250)

                        if (gold_taken == 1):
                            Win()
main(WIN, WIDTH)
