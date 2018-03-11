""" Contains Snake and Apple """
import graphics_handler

class Snake(object):
	"""User controlled object that consists of squares.
	
	Color can be passed with Snake(color)
	Snake's main properties are its location_list, length, and score."""

	# color 			- the color of the blocks drawn by the snake
	# length 			- how many blocks the snake is made of
	# score				- each snake is applied one-per-player, so the easiest mode of storage is in snake
	# position_record	- list (used as queue instead of stack) of the ```SIMPLIFIED``` coordinates

	def __init__(self, win, color="red"):
		self.length = 1
		self.color = color
		# Get grid
		start_point = graphics_handler.get_center_grid(win)
		# This is intentionally a nested array.
		self.position_record = [start_point]
		# Draw said position
		graphics_handler.draw_square_from_grid(win, start_point)




class Apple(object):
	pass
