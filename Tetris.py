import pygame
from pygame.locals import *

blocks = [
    [[1,4,7],[3,4,5]], #straight
    [[1,3,4,5,7]], #cross
    [[0,1,4,5],[1,3,4,6]], #two on two 1
    [[1,2,3,4],[0,3,4,7]], #two on two 2
    [[0,1,3,6],[0,1,2,5],[2,5,7,8],[3,6,7,8]], #L shape 1
    [[1,2,5,8],[5,6,7,8],[0,3,6,7],[0,1,2,3]], #L shape 2
    [[4,6,7,8],[0,3,4,6],[0,1,2,4],[2,4,5,8]] #one on three
]



class Block:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.type = 0
        self.rotation = 0

    def shape(self):
        return blocks[self.type][self.rotation]

def draw_block():
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                pygame.draw.rect(screen,(255,255,255), 
                [(x + block.x) * grid_size + gap_width + 1, (y + block.y) * grid_size + gap_height + 1,
                grid_size-2, grid_size-2])       

def draw_grid_beta(rows, cols, grid_size):
    for y in range(rows): #rows
        for x in range(cols):#cols
            pygame.draw.rect(screen,(100,100,100), [x*grid_size,y*grid_size, grid_size,grid_size],1)

def draw_grid(colour = (100,100,100)):
    for y in range(rows): #rows
        for x in range(cols):#cols
            pygame.draw.rect(screen, colour, [x * grid_size + gap_width, y * grid_size + gap_height, 
            grid_size, grid_size], 1)
            if game_board[x][y] != (0,0,0):
                pygame.draw.rect(screen, game_board[x][y], 
                [x * grid_size + gap_width+1, y * grid_size + gap_height+1, grid_size-1, grid_size-1])      #draw the game board

def drop_block():
    can_drop = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():  #checking existing x's and y's in the shape
                if block.y + y >= rows - 1: #if touching the bottom of the screen
                    can_drop = False
    if can_drop:
        block.y+=1
    else:
        for y in range(3):
            for x in range(3):
                if y * 3 + x in block.shape():
                    game_board[x + block.x][y + block.y] = (0,255,0)
    return can_drop

def side_move(dx):
    can_move_left = True
    can_move_right = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():  #checking existing x's and y's in the shape
                if block.x <= 0: #if touching the left side of the grid
                    can_move_left = False
                if block.x + x >= cols - 1: #if touching the right side of the grid
                    can_move_right = False
    if can_move_left and dx<0:
        block.x += dx
    if can_move_right and dx>0:
        block.x += dx
   



pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("Tetris")
game_over = False
grid_size = 30
cols = screen.get_width()//grid_size
rows = screen.get_height()//grid_size
gap_width = (screen.get_width() - cols*grid_size)//2
gap_height = (screen.get_height() - rows*grid_size)//2
block = Block(2,3) #instance of Block class
block.type = 4
block.rotation=1
clock = pygame.time.Clock()
fps = 5 #frames per second
game_board = []
#initialise game board
for i in range(cols):
    new_col = []
    for j in range(rows):
        new_col.append((0,0,0))
    game_board.append(new_col)


while not game_over:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            continue
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            side_move(-1)
        if event.key == pygame.K_RIGHT:
            side_move(1)
    screen.fill((0,0,0))
    draw_grid()
    if block is not None:
        draw_block()
        if event.type != pygame.KEYDOWN:
            if not drop_block():
                block = None

    pygame.display.update()
pygame.quit()