import pygame
import os
import sys
import random

size = width, height = 900, 600
pygame.init()
pygame.display.set_caption("CoLoR SwItCh")

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 15
global all_stars
start_level = int(open('data/start_level.txt', 'r', encoding='utf-8').read())
all_stars = int(open('data/all_stars.txt', 'r', encoding='utf-8').read())
levels = 10
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and (event.mod & pygame.KMOD_LCTRL):
                    rules()
                    Start_screen()
                elif event.key != pygame.K_d and (event.key != pygame.K_LCTRL):
                    to_game(start_level)

        pygame.display.flip()


def rules():
    size = width, height = 900, 600
    screen = pygame.display.set_mode(size)
    background = load_image("rules.png")
    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        pygame.display.flip()


def completed_screen():
    background = load_image("completed.png")
    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                return
        pygame.display.flip()


def congratulation_screen():
    background = load_image('congratulations.png')
    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    terminate()
        pygame.display.flip()


def game_over(name, i):
    background = load_image("game_over.png")
    screen.blit(background, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                to_game(i)
        pygame.display.flip()


def load_level(name):
    fullname = "data/" + name
    with open(fullname, 'r') as map:
        level_map = []
        for line in map:
            line = line.strip()
            level_map.append(line)
    return level_map


def draw_level(level_map, a, s):
    global star_in_this_level1, star_in_this_level2
    star_in_this_level1 = []
    star_in_this_level2 = []
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
                circle2 = Circle2(x, y, s)
                screen.blit(circle2.c2_rot, circle2.c2_rot_rect)
            elif level_map[y][x] == "!":
                cross = Cross(x, y, a)
                screen.blit(cross.cr_rot, cross.cr_rot_rect)
            elif level_map[y][x] == "*":
                star = Star(x, y, a)
                if x > 15:
                    star_in_this_level2.append(y)
                else:
                    star_in_this_level1.append(y)
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
        self.rot_rect = self.rot.get_rect(centerx=x * 30 + 15, centery=y * 30 + 15)


class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.crcl = load_image("circle1.png")
        self.crcl_rot = pygame.transform.rotate(self.crcl, a)
        self.crcl_rot_rect = self.crcl_rot.get_rect(centerx=x * 30 + 15, centery=y * 30 + 15)


class Sqw(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.squ = load_image("sqw.png")
        self.img = pygame.transform.scale(self.squ, (self.squ.get_width() // 2.5, self.squ.get_height() // 2.5))
        self.squ_rot = pygame.transform.rotate(self.img, a)
        self.squ_rot_rect = self.squ_rot.get_rect(centerx=x * 30 + 15, centery=y * 30 - 15)


class Circle2(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.circ2 = load_image("circle2.png")
        self.img = pygame.transform.scale(self.circ2, (self.circ2.get_width() // 1.5, self.circ2.get_height() // 1.5))
        self.c2_rot = pygame.transform.rotate(self.img, a)
        self.c2_rot_rect = self.c2_rot.get_rect(centerx=x * 30 + 15, centery=y * 30 - 15)


class Cross(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.cross = load_image("cross.png")
        self.img = pygame.transform.scale(self.cross, (self.cross.get_width() // 2, self.cross.get_height() // 2))
        self.cr_rot = pygame.transform.rotate(self.img, a)
        self.cr_rot_rect = self.cr_rot.get_rect(centerx=x * 30 - 40, centery=y * 30 + 15)


class Star(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.star = load_image("star.png")
        self.img = pygame.transform.scale(self.star, (self.star.get_width() // 7, self.star.get_height() // 7))
        self.st_rot = pygame.transform.rotate(self.img, a)
        self.st_rot_rect = self.st_rot.get_rect(centerx=x * 30 + 15, centery=y * 30 - 15)


class Start_Finish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sf = load_image("start_finish.png")
        self.sf_r = self.sf.get_rect(center=(x * 225, y))


def game(name, i):
    global star_in_this_level1, star_in_this_level2, all_stars
    board = Board(30, 20)
    board.set_view(0, 0, 30)
    size = width, height = 900, 600
    screen = pygame.display.set_mode(size)
    colors = [(195, 45, 255), (124, 255, 137), (0, 255, 242), (255, 255, 0)]
    a = 20
    s = 20
    f = 0
    e = 0
    z = 0
    m = True
    start = Start_Finish(0.88, 495)
    finish = Start_Finish(3.12, 100)
    collect_stars = []
    running = True
    flag = False
    y = 535
    part = 1
    lvl = "_-_-LeVeL " + f'{i} -_-_'
    lvl_font = pygame.font.SysFont('couriernew', 40)
    lvl_font.set_bold(True)
    lvl_start = lvl_font.render(lvl, True, (255, 255, 255))
    lvl_finish = lvl_font.render(lvl, True, (255, 255, 255))
    while running:
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.draw.rect(screen, (255, 255, 255), (449, 0, 2, 600))
        draw_level(load_level(name), a, s)
        for aaa in collect_stars:
            if aaa[0] == 1:
                pygame.draw.rect(screen, 'black', [30 * 7 + 1, 30 * (aaa[1] - 1) + 1, 28, 28])
            else:
                pygame.draw.rect(screen, 'black', [30 * 22 + 1, 30 * (aaa[1] - 1) + 1, 28, 28])
        screen.blit(lvl_start, (0, 555))
        screen.blit(lvl_finish, (450, 0))
        screen.blit(start.sf, start.sf_r)
        screen.blit(finish.sf, finish.sf_r)
        a += 3
        s += 5
        if f == 0:
            e = colors[random.randint(0, 3)]
            f += 1
        if f == 1:
            z = colors[random.randint(0, 3)]
            f += 1
        if m:
            if part == 2:
                if y <= 540:
                    pygame.draw.circle(screen, e, (675, y), 15)
                else:
                    pygame.draw.circle(screen, z, (675, y), 15)
            else:
                if y <= 450:
                    pygame.draw.circle(screen, z, (225, y), 15)
                else:
                    pygame.draw.circle(screen, (255, 255, 255), (225, y), 15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y -= 25
                flag = True
        if flag:
            if part == 2 and y < 85:
                y -= 5
            y += 3

        if y < 0:
            if part == 1:
                part = 2
                y += 600
            else:
                all_stars += len(collect_stars)
                with open('data/all_stars.txt', 'w', encoding='utf-8') as f:
                    print(str(all_stars), file=f)
                return
        if y > 600:
            if part == 2:
                part = 1
                y -= 600
            elif part == 1:
                game_over(name, i)
        if part == 1:
            for aaa in star_in_this_level1:
                if y < aaa * 30 - 15 and [1, aaa] not in collect_stars:
                    collect_stars.append([1, aaa])
        else:
            for aaa in star_in_this_level2:
                if y < aaa * 30 - 15 and [2, aaa] not in collect_stars:
                    collect_stars.append([2, aaa])
        pygame.display.flip()
        clock.tick(fps)


def to_game(start_level):
    for i in range(start_level, levels + 1):
        game(f'level{i}.txt', i)
        if i < levels:
            start_level += 1
            with open('data/start_level.txt', 'w', encoding='utf-8') as f:
                print(str(start_level), file=f)
            completed_screen()
        else:
            with open('data/start_level.txt', 'w', encoding='utf-8') as f:
                print('1', file=f)
            congratulation_screen()


Start_screen()
