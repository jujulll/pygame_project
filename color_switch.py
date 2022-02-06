import pygame
import os
import sys
import random

size = width, height = 868, 685
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
    background = load_image("start_screen.png")
    screen.blit(background, (-1, 1))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                Level_01()
        pygame.display.flip()


def completed_screen():
    size = width, height = 700, 524
    screen = pygame.display.set_mode(size)
    background = load_image("comp.png")
    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                return
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
                change = Change_color(x, y, a)
                screen.blit(change.rot, change.rot_rect)
            elif level_map[y][x] == "&":
                circle = Circle(x, y, a)
                screen.blit(circle.crcl_rot, circle.crcl_rot_rect)
            elif level_map[y][x] == "?":
                square = Sqw(x, y, a)
                screen.blit(square.squ_rot, square.squ_rot_rect)
            elif level_map[y][x] == "$":
                circle2 = Circle2(x, y, a)
                screen.blit(circle2.c2_rot, circle2.c2_rot_rect)
            elif level_map[y][x] == "!":
                cross = Cross(x, y, a)
                screen.blit(cross.cr_rot, cross.cr_rot_rect)
            elif level_map[y][x] == "*":
                star = Star(x, y, a)
                screen.blit(star.st_rot, star.st_rot_rect)


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
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("change.png")
        self.img = pygame.transform.scale(self.image, (self.image.get_width() * 0.75, self.image.get_height() * 0.75))
        self.rot = pygame.transform.rotate(self.img, a)
        self.rot_rect = self.rot.get_rect(centerx=x * 30, centery=y * 30 + 10)


class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.crcl = load_image("circle1.png")
        self.crcl_rot = pygame.transform.rotate(self.crcl, a)
        self.crcl_rot_rect = self.crcl_rot.get_rect(centerx=x * 30, centery=y * 30)


class Sqw(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.squ = load_image("sqw.png")
        self.img = pygame.transform.scale(self.squ, (self.squ.get_width() // 2.5, self.squ.get_height() // 2.5))
        self.squ_rot = pygame.transform.rotate(self.img, a)
        self.squ_rot_rect = self.squ_rot.get_rect(centerx=x * 30, centery=y * 30)


class Circle2(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.circ2 = load_image("circle2.png")
        self.img = pygame.transform.scale(self.circ2, (self.circ2.get_width() // 1.5, self.circ2.get_height() // 1.5))
        self.c2_rot = pygame.transform.rotate(self.img, a)
        self.c2_rot_rect = self.c2_rot.get_rect(centerx=x * 30, centery=y * 30)


class Cross(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.cross = load_image("cross.png")
        self.img = pygame.transform.scale(self.cross, (self.cross.get_width() // 2, self.cross.get_height() // 2))
        self.cr_rot = pygame.transform.rotate(self.img, a)
        self.cr_rot_rect = self.cr_rot.get_rect(centerx=x * 23, centery=y * 30)


class Star(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.star = load_image("star.png")
        self.img = pygame.transform.scale(self.star, (self.star.get_width() // 5, self.star.get_height() // 5))
        self.st_rot = pygame.transform.rotate(self.img, a)
        self.st_rot_rect = self.st_rot.get_rect(centerx=x * 30, centery=y * 30)


class Start_Finish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sf = load_image("start_finish.png")
        self.sf_r = self.sf.get_rect(center=(x * 225, y))


def game(name):
    board = Board(30, 18)
    board.set_view(0, 0, 30)
    size = width, height = 900, 540
    screen = pygame.display.set_mode(size)
    colors = [(195, 45, 255), (124, 255, 137), (0, 255, 242), (255, 255, 0)]
    a = 20
    f = 0
    e = 0
    z = 0
    m = True
    start = Start_Finish(0.88, 15)
    finish = Start_Finish(3.12, 525)
    running = True
    flag = False
    y = 525
    part = 2
    while running:
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.draw.rect(screen, (200, 200, 87), (449, 0, 2, 540))
        draw_level(load_level(name), a)

        screen.blit(start.sf, start.sf_r)
        screen.blit(finish.sf, finish.sf_r)
        a += 3
        if m:
            if part == 2:
                pygame.draw.circle(screen, 'white', (675, y), 15)
            else:
                pygame.draw.circle(screen, 'white', (225, y), 15)
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
        #if 838 > y > 665:
            #pygame.draw.circle(screen, e, (254, y), 15)
            #m = False
        #if y < 665:
            #pygame.draw.circle(screen, z, (254, y), 15)
        if y < 0:
            if part == 2:
                part = 1
                y += 540
            else:
                return
        pygame.display.flip()
        clock.tick(fps)


def Level_01():
    game('level1.txt')
    completed_screen()
    Level_02()


def Level_02():
    game('level2.txt')
    completed_screen()
    Level_03()


def Level_03():
    game('level3.txt')


Start_screen()