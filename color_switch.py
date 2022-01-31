import pygame
import os
import sys
import random

size = width, height = 356, 545
pygame.init()
pygame.display.set_caption("CoLoR SwItCh")

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 15
screen.fill((0, 0, 0))


def terminate():
    pygame.quit()
    sys.exit()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def Start_screen():
    background = load_image("start_screen1.png")
    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                Level_01()
        pygame.display.flip()


def load_level(name):
    fullname = "data/" + name
    with open(fullname, 'r') as map:
        level_map = []
        for line in map:
            line = line.strip()
            level_map.append(line)
    return level_map


def draw_level(level_map, a):
    for y in range(len(level_map)):
        for x in range(len(level_map[y])):
            if level_map[y][x] == "#":
                change = Change_color(y, a)
                screen.blit(change.rot, change.rot_rect)
            elif level_map[y][x] == "&":
                circle = Circle(y, a)
                screen.blit(circle.crcl_rot, circle.crcl_rot_rect)


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[1] * width for _ in range(height)]

        self.x = 10
        self.y = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.x = left
        self.y = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(64, 64, 64), (
                    x * self.cell_size + self.x, y * self.cell_size + self.y, self.cell_size, self.cell_size),
                                 self.board[y][x])


class Change_color(pygame.sprite.Sprite):
    def __init__(self, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("change.png")
        self.img = pygame.transform.scale(self.image, (self.image.get_width() * 0.75, self.image.get_height() * 0.75))
        self.rot = pygame.transform.rotate(self.img, a)
        self.rot_rect = self.rot.get_rect(centerx=253, centery=y * 30 + 10)


class Circle(pygame.sprite.Sprite):
    def __init__(self, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.crcl = load_image("circle1.png")
        self.crcl_rot = pygame.transform.rotate(self.crcl, a)
        self.crcl_rot_rect = self.crcl_rot.get_rect(centerx=252, centery=y * 30)


class Start_Finish(pygame.sprite.Sprite):
    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.sf = load_image("start_finish.png")
        self.sf_r = self.sf.get_rect(center=(250, y))


class Camera:
    def __init__(self, y):
        self.dx = 0
        self.dy = 800

    def update(self):
        self.dy -= 400


def game(name):
    board = Board(16, 35)
    board.set_view(0, 0, 30)
    size = width, height = 480, 1020
    screen = pygame.display.set_mode(size)
    colors = [(195, 45, 255), (124, 255, 137), (0, 255, 242), (255, 255, 0)]
    a = 20
    f = 0
    e = 0
    z = 0
    m = True
    start = Start_Finish(15)
    finish = Start_Finish(945)
    running = True
    flag = False
    y = 985
    while running:
        screen.fill((0, 0, 0))
        board.render(screen)
        draw_level(load_level(name), a)

        screen.blit(start.sf, start.sf_r)
        screen.blit(finish.sf, finish.sf_r)
        a += 3
        if m:
            pygame.draw.circle(screen, (255, 255, 255), (254, y), 15)
        s = 0
        if s == 3:
            s -= 3
        else:
            s += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 25
                flag = True
        if flag:
            y += 3
        if f == 0:
            e = colors[random.randint(0, 3)]
            f += 1
        if f == 1:
            z = colors[random.randint(0, 3)]
            f += 1
        if 838 > y > 665:
            pygame.draw.circle(screen, e, (254, y), 15)
            m = False
        if y < 665:
            pygame.draw.circle(screen, z, (254, y), 15)
        if y < 0:
            return
        pygame.display.flip()
        clock.tick(fps)


def Level_01():
    game('level1.txt')
    Level_02()


def Level_02():
    game('level2.txt')

Start_screen()