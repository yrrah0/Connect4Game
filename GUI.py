import pygame as pg
from Utils import MAIN
import sys

pg.init()
clock = pg.time.Clock()
game = MAIN(80, 7)

screen = pg.display.set_mode((game.screen_size, game.screen_size))
base_rect = pg.Rect((0, game.grid_size), (game.screen_size, game.screen_size - game.grid_count))
pg.draw.rect(screen, game.black, pg.Rect(0, 0, game.screen_size, game.screen_size))
pg.draw.rect(screen, game.blue, base_rect)

for i in game.coordinates:
    for j in game.coordinates:
        pg.draw.circle(screen, game.black, (i, j), game.radius)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if 49 <= event.key <= 55:
                column = int(chr(event.key - 1))
                game.play_turn(screen, column)
                print(game.board)

    pg.display.update()
    clock.tick(120)
