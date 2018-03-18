""" This is just a snake program in a scripting language.

More of a test of ability for large projects than anything."""
from graphics import *
from math import floor
from interface import *


play_area_side_size = 500 	#px, if you change this, you will need to alter the title screen
grid_unit_size = 50 	#px, the size of each 'pixel' (as in the size of a snake body part or apple)
grid_cells_per_side = floor(play_area_side_size / grid_unit_size) #Ideally grid unit size would be a factor of play area side size

def main():
	#create graphic window
	win = GraphWin("Python in Python", play_area_side_size, play_area_side_size)
	win.setBackground("black")
	win.setCoords(0,0, grid_cells_per_side, grid_cells_per_side)

	run_title_screen(win, grid_cells_per_side)
	#waits for enter press, then teardown
	teardown_window(win)

	#####################################################
	#					Gameplay Loop					#
	#####################################################
	# print(type(not game_over))

	game_over = False		
	while not game_over:
		# print('.')
		



		game_over = True

	#if repeat:
	#	main()
	#else:
	#	exit()




main()