import pygame

from random import randint

pygame.init()

resolucao = (500, 500)
screen = pygame.display.set_mode(resolucao)
preto = (0, 0, 0)
screen.fill(preto)
pygame.display.update()


class Frutinha:
    cor = (255, 0, 0)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        x = randint(0, 49) * 10
        y = x
        self.posicao = (x, y)


frutinha = Frutinha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(frutinha.textura, frutinha.posicao)
    pygame.display.update()
