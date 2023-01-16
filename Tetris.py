import pygame
from pygame.locals import *
import random

blocks = [
    [[1,4,7],[3,4,5]], #straight
    [[1,3,4,5,7]], #cross
    [[0,1,4,5],[1,3,4,6]], #two on two 1
    [[1,2,3,4],[0,3,4,7]], #two on two 2
    [[0,1,3,6],[0,1,2,5],[2,5,7,8],[3,6,7,8]], #L shape 1
    [[1,2,5,8],[5,6,7,8],[0,3,6,7],[0,1,2,3]], #L shape 2
    [[4,6,7,8],[0,3,4,6],[0,1,2,4],[2,4,5,8]] #one on three
]

colors = [
    (255,0,0), #red
    (0,255,0), #green
    (0,0,255), #yellow
    (255,0,255), #magenda
    (0,255,255), #cyan
    (255,255,0), #yellow
    (192,192,192) # gray
]

class Block:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.type = random.randint(0,len(blocks)-1)
        self.rotation = 0
        self.color = colors[random.randint(0,len(colors)-1)]

    def shape(self):
        return blocks[self.type][self.rotation]

def draw_block():
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                pygame.draw.rect(screen,block.color, 
                [(x + block.x) * grid_size + gap_width + 1, (y + block.y) * grid_size + gap_height + 1,
                grid_size-2, grid_size-2])       

def rotate():
    last_rotation = block.rotation
    block.rotation = (block.rotation + 1) % len(blocks[block.type])
    can_rotate = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape(): 
                if collides(0,0):
                    can_rotate = False
    if not can_rotate:
        block.rotation = last_rotation


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

def collides(nx,ny):
    collision = False
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():  
                if  0 > y + block.y + ny or y + block.y + ny > rows - 1:
                    collision = True
                    break
                if  0 > x + block.x + nx or x + block.x + nx > cols - 1:
                    collision = True
                    break
                if game_board[x + block.x + nx][y + block.y + ny] != (0,0,0):
                    collision = True
                    break
    return collision

def drop_block():
    can_drop = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():  #checking existing x's and y's in the shape
                if collides(0,1): #if touching the bottom of the screen
                    can_drop = False
    if can_drop:
        block.y+=1
    else:
        for y in range(3):
            for x in range(3):
                if y * 3 + x in block.shape():
                    game_board[x + block.x][y + block.y] = block.color
    return can_drop

def side_move(dx):
    can_move = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():  #checking existing x's and y's in the shape
                if collides(dx,0):  #if touching the side of the grid
                    can_move = False
    if can_move:
        block.x += dx
    else: 
        drop_block()
   

def find_lines():
    lines = 0
    for y in range(rows):
        empty = 0
        for x in range(cols):
            if game_board[x][y] == (0,0,0):
                empty += 1              # checking blank spots in line
        if empty == 0:
            lines += 1   #counting lines
            for y2 in range(y,1, -1): 
                for x2 in range(cols):
                    game_board[x2][y2] = game_board[x2][y2-1] #getting rid of line
    return lines


pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("Tetris")
game_over = False
grid_size = 30
cols = screen.get_width()//grid_size
rows = screen.get_height()//grid_size
gap_width = (screen.get_width() - cols*grid_size)//2
gap_height = (screen.get_height() - rows*grid_size)//2
block = Block((cols-1)//2,0) #instance of Block class
block.type = 4
block.rotation=1
clock = pygame.time.Clock()
fps = 5 #frames per second
pause = False
game_board = []
#initialise game board
for i in range(cols):
    new_col = []
    for j in range(rows):
        new_col.append((0,0,0))
    game_board.append(new_col)


score = 0
font = pygame.font.SysFont('Arial',25,True,False)
font2 = pygame.font.SysFont('Arial',50,True,False)
pause_text = font.render("Paused", True, (255,255,255))
game_over_text = font2.render("GAME OVER", True, (255,255,255))
game_finished = False
got_position = [screen.get_width()//2 - game_over_text.get_width()//2, 
                screen.get_height()//2 - game_over_text.get_height()//2]


while not game_over:
    clock.tick(fps)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate()
            elif event.key == pygame.K_SPACE:
                pause = ~(pause)
            
    if event.type == pygame.KEYDOWN and not pause:
        if event.key == pygame.K_LEFT:
            side_move(-1)
        if event.key == pygame.K_RIGHT:
            side_move(1)
    
    
    if pause:
        screen.blit(pause_text, [screen.get_width()//2 - pause_text.get_width()//2,0])
        pygame.display.update()
        continue

    screen.fill((0,0,0))
    draw_grid()
    if block is not None:
        draw_block()
        if event.type != pygame.KEYDOWN:
            if not drop_block() and not game_finished:
                score += find_lines()
                block = Block(random.randint(2,cols-3),0)
                if collides(0,0):
                    game_finished = True

    
    text = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(text, [0,0])
    if game_finished:
        screen.blit(game_over_text,got_position)
    pygame.display.update()
pygame.quit()