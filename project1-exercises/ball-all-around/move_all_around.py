import pygame

pygame.init
screen = pygame.display.set_mode((800, 600))
img = pygame.image.load('ball.gif')
rect = img.get_rect()
screen_rect = screen.get_rect()
rect.centerx = screen_rect.centerx
rect.centery = screen_rect.centery
moving_right = False
moving_left = False
moving_up = False
moving_down = False
bg_color = '#10AA10'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False
            
    if moving_up and rect.top > screen_rect.top:
        rect.centery -= 1
    if moving_down and rect.bottom < screen_rect.bottom:
        rect.centery += 1
    if moving_left and rect.left > screen_rect.left:
        rect.centerx -= 1
    if moving_right and rect.right < screen_rect.right:
        rect.centerx += 1

    screen.fill(bg_color)
    screen.blit(img, rect)
    pygame.display.flip()

