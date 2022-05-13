from os import path

COLORS = {
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'orange': (255, 165, 0)
}

CAPTION = 'Space Invaders'
WIDTH, HEIGHT = 900, 500
FPS = 60
FONT = {
    'font': 'consolas',
    'size': 15,
    'color': COLORS['black'],
    'destination': (10, 10)
}


class Asset:
    YELLOW_SPACESHIP = {
        'image': path.join('Assets', 'spaceship_yellow.png'),
        'size': (55, 40),
        'rotate': 90,
        'destination': (100, 300)
    }
    RED_SPACESHIP = {
        'image': path.join('Assets', 'spaceship_red.png'),
        'size': (55, 40),
        'rotate': 270,
        'destination': (700, 300)
    }
    BORDER = {'size': (WIDTH / 2 - 5, 0, 2, HEIGHT), 'color': COLORS['black']}
    BULLET = {'size': (10, 5), 'velocity': 10}

