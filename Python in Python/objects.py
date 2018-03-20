class Snake():
	"""User controlled object that consists of squares.
	
	Color can be passed with Snake(color)
	Snake's main properties are its location_list, length, and score."""

	# color 				- the color of the blocks drawn by the snake
	# length 				- how many blocks the snake is made of
	# score					- each snake is applied one-per-player, so the easiest mode of storage is in snake
	# grid_position_record	- queue of grid coords
	# position_record 		- actually pixel coordinates
	#if the directions become heavily used, you can make a dictionary to go from
		#number to its corollary constant
		
	def __init__(self, win, color="green"):
		self.color = color
		self.length = 1
		self.score = 0
		self.grid_position_record = [0,0]