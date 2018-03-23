""" Used for storing global variables to avoid passing too many parameters"""
from graphics import *
from math import floor


def init():
	#instantiate global
	global win 					#GraphWin object that is the game window
	global play_area_side_size 	#px, if you change this, you will need to alter the title screen
	global grid_unit_size		#px, the size of each 'pixel' (as in the size of a snake body part or apple)
	global grid_cells_per_side  #Ideally grid unit size would be a factor of play area side size
	global tick_length			#length of tick in seconds
	global input_dictionary		#stores acceptable input and what they represent
	global entity_grid			#2D array used for collision detection

	#	grid variables
	play_area_side_size = 300 	
	grid_unit_size = 10		
	grid_cells_per_side = floor(play_area_side_size / grid_unit_size) 		
	#	time variables
	tick_length = .5 			#seconds
	#	input dictionary
	input_dictionary = {
		"up": 		["Up", "w", "W"],
		"down": 	["Down", "s", "S"],
		"left": 	["Left", "a", "A"],
		"right":	["Right", "d", "D"]
		}

	win = GraphWin("Python in Python", play_area_side_size, play_area_side_size)
	win.setBackground("black")
	win.setCoords(0,0, grid_cells_per_side, grid_cells_per_side)

	#entity grid
	for y in range(grid_cells_per_side):
		#reset row for next run
		row = [False]

		for x in range(1, grid_cells_per_side):
			row.append(False)

		#instatiate for first row
		if y == 0:
			entity_grid = [row]
		#append for every other row
		else:
			entity_grid.append(row)


def print_entity_grid():
	for row in range(len(entity_grid)):
		print(entity_grid[row][:])
	# print("\n\nentitygridover")