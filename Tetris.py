import pygame

def draw_grid_beta(rows, cols, grid_size):
    for y in range(rows): #rows
        for x in range(cols):#cols
            pygame.draw.rect(screen,(100,100,100), [x*grid_size,y*grid_size, grid_size,grid_size],1)

def draw_grid(grid_size,colour = (100,100,100)):
    cols = screen.get_width()//grid_size
    rows = screen.get_height()//grid_size
    gap_width = (screen.get_width() - cols*grid_size)/2
    gap_height = (screen.get_height() - rows*grid_size)/2

    for y in range(rows): #rows
        for x in range(cols):#cols
            pygame.draw.rect(screen, colour, [x * grid_size + gap_width, y * grid_size + gap_height, 
            grid_size, grid_size], 1)

grid_size = 30
pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("Tetris")
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.fill((0,0,0))
    draw_grid(30)

    pygame.display.update()
pygame.quit()