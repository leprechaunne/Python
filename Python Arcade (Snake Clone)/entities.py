""" Contains Snake and Apple """
import graphics_handler

class Snake(object):
	"""User controlled object that consists of squares.
	
	Color can be passed with Snake(color)
	Snake's main properties are its location_list, length, and score."""

	# color 				- the color of the blocks drawn by the snake
	# length 				- how many blocks the snake is made of
	# score					- each snake is applied one-per-player, so the easiest mode of storage is in snake
	# grid_position_record	- list (used as queue instead of stack) of the Rectangles()
	#							- Cannot stress enough. Its the actual graphics item
	# position_record 		- actually pixel coordinates

	def __init__(self, win, color="green"):
		self.length = 1
		self.color = color
		# Get grid
		start_point = graphics_handler.get_center_grid(win)
		#record this in the pixel position_record
		self.position_record = start_point
		# Draw said position
		self.grid_position_record = [graphics_handler.draw_square_from_grid(win, start_point, self.color)]
		#CAUTION: with >1 snakes, this has to change
			#Probably use center grid, then center grid with the smaller section
			#For four players, repeat twice (which is 2^2)
			#If you really want more players, the splitting 
			#should be repeated i times where i is:
				#		#find nearest_power_of_2 by looping
				#		nearest_power_of_2 = 2
				#		base = 1
				#		
				#		while num_players > nearest_power_of_2:
				#			nearest_power_of_2 = nearest_power_of_2**2
				#			base += 1
				#		
				#		i = base
				#		#base is the number of iterations, though it may generate too many if the
				#		#number of plays is not a power of two
				#		#
				#		# mathematically speaking, log2(next_power_of_2) = i

class Apple(object):
	"""The primary method of gaining score. 

	Eating an apple should increase snake length and increase score."""

	def __init__(self, win, occupied_spaces, color="red"):
		"""constructor"""
		# Get an unused position
		guess = graphics_handler.get_random_grid(win)
		while guess in occupied_spaces:
			guess = graphics_handler.get_random_grid(win)

		# Customize and draw apple
		apple = graphics_handler.draw_square_from_grid(win, guess, color)
