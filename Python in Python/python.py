""" This is just a snake program in a scripting language.

More of a test of ability for large projects than anything."""
from graphics import *
from math import floor
from interface import *
from time import sleep

#	grid variables
play_area_side_size = 500 	#px, if you change this, you will need to alter the title screen
grid_unit_size = 50 		#px, the size of each 'pixel' (as in the size of a snake body part or apple)
grid_cells_per_side = floor(play_area_side_size / grid_unit_size) 		#Ideally grid unit size would be a factor of play area side size
#	time variables
tick_length = .5 			#seconds
#	input dictionary
input_dictionary = {
	"up": 		["Up", "w"],
	"down": 	["Down", "s"],
	"left": 	["Left", "a"],
	"right":	["Right", "d"]
	}

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
		key_pressed = win.checkKey()

		#evaluate input
		x_mod, y_mod = 0, 0

		if key_pressed in input_dictionary("up"):
			y_mod = 1
		elif key_pressed in input_dictionary("down"):
			y_mod = -1
		elif key_pressed in input_dictionary("right"):
			x_mod = 1
		elif key_pressed in input_dictionary("left"):
			x_mod = -1

		
		# game_over = True
		sleep(tick_length)

	#if repeat:
	#	main()
	#else:
	#	exit()




main()