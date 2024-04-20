import pygame
pygame.init()
from classies import Hero1, Hero2, Enemy

def game():
    win.fill((200, 200, 255))
    player_1.move()
    player_2.move()
    player_1.reset()
    player_2.reset()

def endgame():
    pass

win = pygame.display.set_mode((800, 800))
pygame.display.set_caption('PingPong')


player_1 = Hero1('rocket1.png', 700, 200, 10, 50, 200, win)
player_2 = Hero2('rocket2.png', 50, 200, 10, 50, 200, win)

run = True
finish = False
clock = pygame.time.Clock()

while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

        if not finish:
            game()
        else:
            endgame()

    pygame.display.update()
    clock.tick(60)