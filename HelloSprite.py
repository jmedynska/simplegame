import pygame
pygame.init()
screen_width = 700
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32) #Main window
sprite1 = pygame.image.load('./simplegame/images/football.png') #Ball image
sprite2 = pygame.image.load('./simplegame/images/butterfly.png')
sprite2_width = sprite2.get_width()
sprite2_height = sprite2.get_height()

pygame.display.set_caption("Hello Sprite") #Caption on main window
screen.fill((0, 0, 0)) #Black background

game_over = False

#Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    #screen.blit(sprite1, (384, 284)) # ball in the center of the screen
    screen.blit(sprite2, (screen_width/2-sprite2_width/2, screen_height/2 - sprite2_height/2))
    pygame.display.update()
pygame.quit()