import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Breakin' Bricks")

#bat
bat = pygame.image.load('./simplegame/images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()
bat_rect[1] = screen.get_height() - 100  #initial vertical value
bat_rect[0] = (screen.get_width()-bat_rect[2])/2 #initial horizontal value


#ball
ball = pygame.image.load('./simplegame/images/football.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = (200,200)
ball_speed = (3.0,3.0)
ball_served = False
sx, sy = ball_speed
ball_rect.topleft = ball_start

#brick
brick = pygame.image.load('./simplegame/images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []     #empty list
brick_rows = 5
brick_gap = 10
brick_cols = screen.get_width() // (brick_rect[2]+brick_gap) #how many bricks will fit into the screen
side_gap = (screen.get_width() - brick_cols * (brick_rect[2]+brick_gap) + brick_gap)//2

for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_cols):
        brickX = x * (brick_rect[2] + brick_gap)  + side_gap
        bricks.append((brickX,brickY))



clock = pygame.time.Clock()
game_over = False

while not game_over:
    dt = clock.tick(50)
    screen.fill((0,0,0))

    for b in bricks:
        screen.blit(brick, b)

    screen.blit(ball,(ball_rect))
    screen.blit(bat, (bat_rect))
    # bat movement control
    pressed = pygame.key.get_pressed()
    if pressed[K_RIGHT]:
        bat_rect[0] += 0.5 * dt
    if pressed[K_LEFT]:
        bat_rect[0] -= 0.5 * dt
    #screen restriction for bat
    if bat_rect[0] > (screen.get_width()-bat_rect[2]):
        bat_rect[0] = screen.get_width()-bat_rect[2]
    if bat_rect[0] < 0:
        bat_rect[0] = 0
    #ball serve
    if pressed[K_SPACE]:
        ball_served = True
    if ball_served:
        ball_rect[0] += sx
        ball_rect[1] += sy
    #screen restriction for ball
    if ball_rect[0] >= (screen.get_width()-ball_rect[2]):
        ball_rect[0] = screen.get_width()-ball_rect[2]
        sx *= -1
    if ball_rect[0] <= 0:
        ball_rect[0] = 0
        sx *= -1
    if ball_rect[1] >= (screen.get_height()-ball_rect[3]):
        ball_rect[1] = screen.get_height()-ball_rect[3]
        sy *= -1
    if ball_rect[1] <= 0:
        ball_rect[1] = 0
        sy *= -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    pygame.display.update()
        
pygame.quit()