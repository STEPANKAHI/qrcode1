import pygame
from pygame.locals import *
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация кораблика")

clock = pygame.time.Clock()

ship_image = pygame.image.load("ship.png") # Загрузка изображения кораблика
ship_rect = ship_image.get_rect()
ship_rect.center = (WIDTH // 2, HEIGHT // 2)

speed = 5

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        ship_rect.x -= speed
    if keys[K_RIGHT]:
        ship_rect.x += speed
    if keys[K_UP]:
        ship_rect.y -= speed
    if keys[K_DOWN]:
        ship_rect.y += speed

    win.fill((0, 0, 0))  # Очистка экрана

    win.blit(ship_image, ship_rect)  # Отрисовка кораблика

    pygame.display.update()

    clock.tick(FPS)