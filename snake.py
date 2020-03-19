import pygame

from random import randint

pygame.init()

resolucao = (500, 500)
screen = pygame.display.set_mode(resolucao)
preto = (0, 0, 0)
screen.fill(preto)
pygame.display.update()


class Snake:
    cor = (255, 255, 255)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.corpo = [(100, 100), (90, 100), (80, 100)]

    def blit(self):
        for posicao in snake.corpo:
            screen.blit(self.textura, posicao)


class Frutinha:
    cor = (255, 0, 0)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        x = randint(0, 49) * 10
        y = x
        self.posicao = (x, y)

    def blit(self):
        screen.blit(self.textura, self.posicao)


frutinha = Frutinha()
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    frutinha.blit()
    snake.blit()

    pygame.display.update()
