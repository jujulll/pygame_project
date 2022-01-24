import pygame
import os
import sys
import random


size = width, height = 500, 1000
pygame.init()
pygame.display.set_caption("CoLoR SwItCh")

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 15
screen.fill((0, 0, 0))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Change_color(pygame.sprite.Sprite):
    def __init__(self, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("change.png")
        self.img = pygame.transform.scale(self.image, (self.image.get_width() * 0.75, self.image.get_height() * 0.75))
        self.rot = pygame.transform.rotate(self.img, a)
        self.rot_rect = self.rot.get_rect(centerx=248, centery=y * 2)


class Circle(pygame.sprite.Sprite):
    def __init__(self, y, a):
        pygame.sprite.Sprite.__init__(self)
        self.crcl = load_image("circle1.png")
        self.crcl_rot = pygame.transform.rotate(self.crcl, a)
        self.crcl_rot_rect = self.crcl_rot.get_rect(centerx=248, centery=y)


class Start_Finish(pygame.sprite.Sprite):
    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.sf = load_image("start_finish.png")
        self.sf_r = self.sf.get_rect(center=(250, y))


colors = [(195, 45, 255), (124, 255, 137), (0, 255, 242), (255, 255, 0)]
c = (255, 255, 255)
a = 20
b = 10
change1 = Change_color(960, a)
start = Start_Finish(15)
finish = Start_Finish(945)
running = True
flag = False
y = 985
while running:
    screen.fill((0, 0, 0))
    change1 = Change_color(400, a)
    change2 = Change_color(300, a)
    circle1 = Circle(600, b)
    a += 3
    b += 5
    screen.blit(start.sf, start.sf_r)
    screen.blit(finish.sf, finish.sf_r)
    screen.blit(change1.rot, change1.rot_rect)
    screen.blit(change2.rot, change2.rot_rect)
    screen.blit(circle1.crcl_rot, circle1.crcl_rot_rect)
    pygame.draw.circle(screen, (255, 255, 255), (250, y), 15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 25
            flag = True
    if flag:
        y += 3
    
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()