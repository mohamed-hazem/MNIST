import pygame as pg
pg.init()
pg.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BG_COLOR = BLACK

FPS = 240

WIDTH, HEIGHT = 600, 700
ROWS = COLS = 28

TOOLBAR_HEIGHT = HEIGHT - WIDTH
PIXEL_SIZE = WIDTH // COLS


def get_font(size):
    return pg.font.SysFont("comicsans", size)