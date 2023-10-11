import pygame
import pygame.freetype

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 200

screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.freetype.Font("nirmala.ttf", FONT_SIZE)

clock = pygame.time.Clock()
angle = 0

ok = True
while ok:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ok = False

    screen.fill(WHITE)
    text_surface, _ = font.render('इ', BLACK)
    rotated_surface = pygame.transform.rotate(text_surface, angle)
    screen.blit(rotated_surface, (WIDTH // 2 - rotated_surface.get_width() // 2,
                                  HEIGHT // 2 - rotated_surface.get_height() // 2))

    pygame.display.flip()

    angle += 1
    angle %= 360

    clock.tick(60)
