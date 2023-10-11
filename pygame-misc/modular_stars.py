import pygame 

PINK = (200, 20, 140)
YELLOW = (200, 200, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Modular math stars')

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(PINK)
    pygame.draw.circle(screen, YELLOW, (400, 300), 200)

    pygame.display.flip()


pygame.quit()