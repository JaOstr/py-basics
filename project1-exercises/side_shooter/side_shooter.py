import pygame

class Bullet(pygame.sprite.Sprite):
    """Class for managing bullets shot by the ship"""

    def __init__(self, screen, rect):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.centery = rect.centery
        self.rect.left = rect.left

        self.x = float(self.rect.x)

        self.color = (60, 60, 60)

    def update(self):
        self.x += 0.5
        self.rect.x = self.x

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


pygame.init
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('side shooter')
img = pygame.image.load('ship-horizontal.bmp')
rect = img.get_rect()
screen_rect = screen.get_rect()
rect.left = screen_rect.left
rect.centery = screen_rect.centery
moving_up = False
moving_down = False
bg_color = (230, 230, 230)
bullets_allowed = 3
bullets = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
            elif event.key == pygame.K_SPACE:
                if len(bullets) < bullets_allowed:
                    new_bullet = Bullet(screen, rect)
                    bullets.add(new_bullet)            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False
            
    if moving_up and rect.top > screen_rect.top:
        rect.centery -= 1
    if moving_down and rect.bottom < screen_rect.bottom:
        rect.centery += 1

    screen.fill(bg_color)

    bullets.update()
    # remove bullets that went out of screen
    for bullet in bullets.copy():
        if bullet.rect.left  >= screen_rect.right:
            bullets.remove(bullet)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # draw ship
    screen.blit(img, rect)
    pygame.display.flip()
