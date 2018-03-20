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
	play_area_side_size = 500 	
	grid_unit_size = 50 		
	grid_cells_per_side = floor(play_area_side_size / grid_unit_size) 		
	#	time variables
	tick_length = .5 			#seconds
	#	input dictionary
	input_dictionary = {
		"up": 		["Up", "w"],
		"down": 	["Down", "s"],
		"left": 	["Left", "a"],
		"right":	["Right", "d"]
		}

	win = GraphWin("Python in Python", play_area_side_size, play_area_side_size)
	win.setBackground("black")
	win.setCoords(0,0, grid_cells_per_side, grid_cells_per_side)

	


