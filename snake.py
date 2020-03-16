import pygame

pygame.init()

resolucao = (500, 500)
screen = pygame.display.set_mode(resolucao)
preto = (0, 0, 0)
screen.fill(preto)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
