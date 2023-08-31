import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGame keys explorer")

font = pygame.font.SysFont('comicsans', 30)
while True:
    for event in pygame.event.get():
        screen.fill('#885588')
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            txt = font.render("Key: " + str(event.key), True, 'yellow')
            screen.blit(txt, (250, 280))
        pygame.display.flip()
