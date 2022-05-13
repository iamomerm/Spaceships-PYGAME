#  _______  __   __  _______  _______  __   __  _______
# |       ||  | |  ||       ||   _   ||  |_|  ||       |
# |    _  ||  |_|  ||    ___||  |_|  ||       ||    ___|
# |   |_| ||       ||   | __ |       ||       ||   |___
# |    ___||_     _||   ||  ||       ||       ||    ___|
# |   |      |   |  |   |_| ||   _   || ||_|| ||   |___
# |___|      |___|  |_______||__| |__||_|   |_||_______|
# Pygame is a 2D Graphics Easy-to-Operate Game Engine

import pygame
import spec

pygame.init()

# Spec
WIN = pygame.display.set_mode((spec.WIDTH, spec.HEIGHT))
pygame.display.set_caption(spec.CAPTION)
FONT = pygame.font.SysFont(spec.FONT['font'], spec.FONT['size'])
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
yellow_score = 0
red_score = 0

# Assets
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(pygame.image.load(spec.Asset.YELLOW_SPACESHIP['image']),
                           spec.Asset.YELLOW_SPACESHIP['size']),
    spec.Asset.YELLOW_SPACESHIP['rotate'])

RED_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(pygame.image.load(spec.Asset.RED_SPACESHIP['image']),
                           spec.Asset.RED_SPACESHIP['size']),
    spec.Asset.RED_SPACESHIP['rotate'])


def draw_window(yellow_spaceship_rect, red_spaceship_rect, yellow_spaceship_bullets, red_spaceship_bullets):
    WIN.fill((255, 255, 255))
    WIN.blit(FONT.render("Yellow: %d, Red: %d" % (yellow_score, red_score), False, spec.FONT['color']),
             spec.FONT['destination'])
    for bullet in yellow_spaceship_bullets:
        pygame.draw.rect(WIN, spec.COLORS['orange'], bullet)
    for bullet in red_spaceship_bullets:
        pygame.draw.rect(WIN, spec.COLORS['red'], bullet)
    pygame.draw.rect(WIN, spec.Asset.BORDER['color'], spec.Asset.BORDER['size'])
    WIN.blit(YELLOW_SPACESHIP, (yellow_spaceship_rect.x, yellow_spaceship_rect.y))
    WIN.blit(RED_SPACESHIP, (red_spaceship_rect.x, red_spaceship_rect.y))
    pygame.display.update()  # Update Display


red_spaceship_handle_direction = [3]


def red_spaceship_handle(red_spaceship_rect):
    if red_spaceship_rect.y > spec.HEIGHT - 60:
        red_spaceship_handle_direction[0] = -3
    elif red_spaceship_rect.y < 15:
        red_spaceship_handle_direction[0] = 3
    return red_spaceship_handle_direction[0]


yellow_spaceship_bullets = []
red_spaceship_bullets = []


def yellow_spaceship_handle(keys, yellow_spaceship_rect):
    if keys[pygame.K_LEFT] and yellow_spaceship_rect.x - 20 > 0:
        yellow_spaceship_rect.x -= 5
    elif keys[pygame.K_RIGHT] and yellow_spaceship_rect.x + 20 < spec.Asset.BORDER['size'][0] - 40:
        yellow_spaceship_rect.x += 5
    elif keys[pygame.K_DOWN] and yellow_spaceship_rect.y + 20 < spec.HEIGHT - 60:
        yellow_spaceship_rect.y += 5
    elif keys[pygame.K_UP] and yellow_spaceship_rect.y - 20 > 15:
        yellow_spaceship_rect.y -= 5


def yellow_spaceship_fire_handle(yellow_spaceship_rect):
    yellow_spaceship_bullets.append(
        pygame.Rect(yellow_spaceship_rect.x, yellow_spaceship_rect.y + spec.Asset.YELLOW_SPACESHIP['size'][1] / 2 + 4,
                    spec.Asset.BULLET['size'][0], spec.Asset.BULLET['size'][1]))


def yellow_spaceship_bullet_handle(red_spaceship_rect):
    for bullet in yellow_spaceship_bullets:
        bullet.x += spec.Asset.BULLET['velocity']
        if red_spaceship_rect.colliderect(bullet):
            globals()['yellow_score'] += 1


def red_spaceship_fire_handle(red_spaceship_rect):
    red_spaceship_bullets.append(
        pygame.Rect(red_spaceship_rect.x, red_spaceship_rect.y + spec.Asset.RED_SPACESHIP['size'][1] / 2 + 4,
                    spec.Asset.BULLET['size'][0], spec.Asset.BULLET['size'][1]))


def red_spaceship_bullet_handle(yellow_spaceship_rect):
    for bullet in red_spaceship_bullets:
        bullet.x -= spec.Asset.BULLET['velocity']
        if yellow_spaceship_rect.colliderect(bullet):
            globals()['red_score'] += 1


def main():
    # Game
    yellow_spaceship_rect = pygame.Rect(spec.Asset.YELLOW_SPACESHIP['destination'][0],
                                        spec.Asset.YELLOW_SPACESHIP['destination'][1],
                                        spec.Asset.YELLOW_SPACESHIP['size'][0], spec.Asset.YELLOW_SPACESHIP['size'][1])

    red_spaceship_rect = pygame.Rect(spec.Asset.RED_SPACESHIP['destination'][0],
                                     spec.Asset.RED_SPACESHIP['destination'][1],
                                     spec.Asset.RED_SPACESHIP['size'][0], spec.Asset.RED_SPACESHIP['size'][1])

    clock = pygame.time.Clock()
    run = True
    timer = 0
    while run:
        clock.tick(spec.FPS)
        timer = timer + 1 if timer < 60 else 0

        # Red Spaceship Handling
        red_spaceship_rect.y += red_spaceship_handle(red_spaceship_rect)

        # Yellow Spaceship Handling
        keys = pygame.key.get_pressed()
        yellow_spaceship_handle(keys, yellow_spaceship_rect)  # Keypressed for Smoother Movement

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:  # Keydown for Single Click = Single Event
                if event.key == pygame.K_SPACE:
                    yellow_spaceship_fire_handle(yellow_spaceship_rect)

        # Run
        yellow_spaceship_bullet_handle(red_spaceship_rect)
        if timer % 10 == 0:
            red_spaceship_fire_handle(red_spaceship_rect)
        red_spaceship_bullet_handle(yellow_spaceship_rect)

        draw_window(yellow_spaceship_rect, red_spaceship_rect, yellow_spaceship_bullets, red_spaceship_bullets)
    pygame.quit()


if __name__ == '__main__':
    main()
