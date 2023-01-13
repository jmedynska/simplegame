import pygame

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
block.type = 3
block.rotation=1
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.fill((0,0,0))
    draw_grid()
    draw_block()

    pygame.display.update()
pygame.quit()