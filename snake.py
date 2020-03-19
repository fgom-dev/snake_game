import random
from time import sleep

import pygame

pygame.init()

resolucao = (500, 500)
screen = pygame.display.set_mode(resolucao)
pygame.display.set_caption(f'Snake - Pontuação: 0')
preto = (0, 0, 0)
clock = pygame.time.Clock()


class Snake:
    cor = (255, 255, 255)
    tamanho = (10, 10)
    velocidade = 10

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.corpo = [(100, 100), (90, 100), (80, 100)]

        self.direcao = 'direita'

        self.pontos = 0

        pygame.display.set_caption(f'Snake - Pontuação: {self.pontos}')

    def blit(self, screen):
        for posicao in snake.corpo:
            screen.blit(self.textura, posicao)

    def andar(self):
        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]

        if self.direcao == 'direita':
            self.corpo.insert(0, (x + self.velocidade, y))
        elif self.direcao == 'esquerda':
            self.corpo.insert(0, (x - self.velocidade, y))
        elif self.direcao == 'cima':
            self.corpo.insert(0, (x, y - self.velocidade))
        elif self.direcao == 'baixo':
            self.corpo.insert(0, (x, y + self.velocidade))

        self.corpo.pop(-1)

    def cima(self):
        if self.direcao != 'baixo':
            self.direcao = 'cima'

    def baixo(self):
        if self.direcao != 'cima':
            self.direcao = 'baixo'

    def esquerda(self):
        if self.direcao != 'direita':
            self.direcao = 'esquerda'

    def direita(self):
        if self.direcao != 'esquerda':
            self.direcao = 'direita'

    def colisao_frutinha(self, frutinha):
        return self.corpo[0] == frutinha.posicao

    def comer(self):
        self.corpo.append((0, 0))
        self.pontos += 1
        pygame.display.set_caption(f'Snake - Pontuação: {self.pontos}')

    def colisao(self):
        cabeca = self.corpo[0]
        x = cabeca[0]
        y = cabeca[1]

        return x < 0 or y < 0 or x > 490 or y > 490 or cabeca in self.corpo[1:]


class Frutinha:
    cor = (255, 0, 0)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        x = random.randint(0, 49) * 10
        y = x
        self.posicao = (x, y)

    def blit(self, screen):
        screen.blit(self.textura, self.posicao)


frutinha = Frutinha()
snake = Snake()

while True:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.cima()
                break
            elif event.key == pygame.K_DOWN:
                snake.baixo()
                break
            elif event.key == pygame.K_LEFT:
                snake.esquerda()
                break
            elif event.key == pygame.K_RIGHT:
                snake.direita()
                break

    if snake.colisao_frutinha(frutinha):
        snake.comer()
        frutinha = Frutinha()

    if snake.colisao():
        sleep(2)
        snake = Snake()


    snake.andar()
    screen.fill(preto)
    frutinha.blit(screen)
    snake.blit(screen)


    pygame.display.update()
