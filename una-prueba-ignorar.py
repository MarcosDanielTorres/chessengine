import pygame

pygame.init() 
  
canvas = pygame.display.set_mode((1024, 720)) 
  
pygame.display.set_caption("My Board") 
exit = False

board = [
    ['R', 'N', 'B', 'Q' ,'K' ,'B' ,'N' ,'R'],
    ['P', 'P', 'P', 'P' ,'P' ,'P' ,'P' ,'P'],
    ['0', '0', '0', '0' ,'0' ,'0' ,'0' ,'0'],
    ['0', '0', '0', '0' ,'0' ,'0' ,'0' ,'0'],
    ['0', '0', '0', '0' ,'0' ,'0' ,'0' ,'0'],
    ['0', '0', '0', '0' ,'0' ,'0' ,'0' ,'0'],
    ['P', 'P', 'P', 'P' ,'P' ,'P' ,'P' ,'P'],
    ['R', 'N', 'B', 'K' ,'Q' ,'B' ,'N' ,'R'],
]

  
white = (255, 255, 255)
red = (255, 0, 0)

while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True

    rect = pygame.Rect(100, 100, 200, 150)
    pygame.draw.rect(canvas, red, rect, width=0)
    pygame.display.update()
    print(board)