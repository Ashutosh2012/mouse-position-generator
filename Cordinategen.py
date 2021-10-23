import pygame as pg
import sys

screenwidth = int( input( "Enter a number : " ) )
screenheight = int( input( "Enter a number : " ) )
screen = pg.display.set_mode( ( screenwidth , screenheight ) )
pg.display.set_caption( "MOUSE POSITION GENERATOR" )

while True:

	for e in pg.event.get():
		if e.type == pg.QUIT:
			sys.exit()
		if e.type == pg.MOUSEBUTTONDOWN:
			pos = pg.mouse.get_pos()
			posX = pos[0]
			posy = pos[1]
			print(f"x : {posX} y : {posy}")
