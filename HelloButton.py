import pygame

pygame.init()
screen = pygame.display.set_mode((500,500), 0, 32)
pygame.display.set_caption("Hello Button")

game_over = False
text_color = (255,255,255)
button_color = (0,0,170)
button_over_color = (255,50,50)
button_width = 100
button_height = 50

button_rect = [screen.get_width()/2 - button_width/2, 
(screen.get_height() - button_height)/2,
button_width, button_height]                        #rectangle

button_font = pygame.font.SysFont('Arial', 20)
button_text = button_font.render('Quit', True, text_color)

screen.fill((100, 100, 100))
x,y = (0,0)
#Main loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if (button_rect[0] <= x <= button_rect[0] + button_rect[2] and
               button_rect[1] <= y <= button_rect[1] + button_rect[3]):
                game_over=True
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            
    if (button_rect[0] <= x <= button_rect[0] + button_rect[2] and
       button_rect[1] <= y <= button_rect[1] + button_rect[3]):
        pygame.draw.rect(screen,button_over_color,button_rect)
    else:
        pygame.draw.rect(screen,button_color,button_rect)

    screen.blit(button_text,
    (button_rect[0] + (button_width - button_text.get_width())/2, 
    button_rect[1] + (button_height- button_text.get_height())/2))  #center text in the button

    pygame.display.update()
pygame.quit()