import pygame
pygame.init()

screen = pygame.display.set_mode((800,600), 0, 32) #Main window
sprite1 = pygame.image.load('./simplegame/images/football.png') #Ball image

pygame.display.set_caption("Hello Sprite") #Caption on main window
screen.fill((0, 0, 0)) #Black background

game_over = False

#Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite1, (384, 284))
    pygame.display.update()
pygame.quit()