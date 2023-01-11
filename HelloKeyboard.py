import pygame
from pygame.locals import *
pygame.init()
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32) #Main window
sprite1 = pygame.image.load('./simplegame/images/football.png') #Ball image
sprite2 = pygame.image.load('./simplegame/images/butterfly.png')
sprite2_width = sprite2.get_width()
sprite2_height = sprite2.get_height()
sprite2 = pygame.transform.scale(sprite2,(32,32)) #Resizing object
pygame.display.set_caption("Hello Keyboard") #Caption on main window
screen.fill((0, 0, 0)) #Black background

game_over = False
x, y = (0,0)
#Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite2, (x,y))
    pygame.display.update()
pygame.quit()