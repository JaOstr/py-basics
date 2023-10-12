import pygame

def rotate_points(points, center, angle):
    pp = pygame.math.Vector2(center)
    rotated_points = [
        (pygame.math.Vector2(x, y) - pp).rotate(angle) + pp for x, y in points]
    return rotated_points


pygame.init()

WIDTH = 1024
HEIGHT = 800

RECT_HEIGHT = 400
RECT_WIDTH = 400
LINE_WIDTH = 2
BLUE = (20, 20, 200)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stellations ending in squares")

screen.fill((70, 70, 0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    square = (((WIDTH - RECT_WIDTH) // 2, (HEIGHT - RECT_HEIGHT) // 2),
              ((WIDTH + RECT_WIDTH) // 2, (HEIGHT - RECT_HEIGHT) // 2),
              ((WIDTH + RECT_WIDTH) // 2, (HEIGHT + RECT_HEIGHT) // 2),
              ((WIDTH - RECT_WIDTH) // 2, (HEIGHT + RECT_HEIGHT) // 2))

    pygame.draw.polygon(screen, BLUE, square, LINE_WIDTH)
    for i in range(1, 4):
        square1 = rotate_points(square, (WIDTH//2, HEIGHT//2), i * 22.5)
        pygame.draw.polygon(screen, BLUE, square1, LINE_WIDTH)


    pygame.display.flip()
