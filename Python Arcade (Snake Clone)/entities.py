""" Contains Snake and Apple """
import graphics_handler
from random import randint


############	Snake Direction Constants ###############
DIRECTION_UP, DIRECTION_RIGHT, DIRECTION_DOWN, DIRECTION_LEFT = 0, 1, 2, 3

##

class Snake(object):
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
	ent_type = "Snake" #it's casting to Rectangle

	def __init__(self, win, color="green"):
		self.length = 1
		self.color = color
		# Get grid
		start_point = graphics_handler.get_center_grid(win)
		#record this in the pixel position_record
		self.grid_position_record = [start_point]
		# Draw said position
		self.rectangle_record = [graphics_handler.draw_square_from_grid(win, start_point, self.color)]
		self.score = 0
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
		self.direction = randint(0, 3)

	def move_direction(self, win, ent_grid):
		"""Called upon moving snake"""
		#check for apple collision
		###check for next position
		xmod, ymod = 0, 0

		if self.direction == DIRECTION_UP:
			ymod = -1
		elif self.direction == DIRECTION_DOWN:
			ymod = 1
		elif self.direction == DIRECTION_LEFT:
			xmod = -1
		elif self.direction == DIRECTION_RIGHT:
			xmod = 1
		else:
			raise Exception("Snake.direction must be 0-3.")

		current_grid_position = self.grid_position_record[0]
		# print(current_grid_position)
		next_grid_position = [current_grid_position[0] + xmod, current_grid_position[1] + ymod]
		
		try: 
			next_ent = ent_grid[next_grid_position[1]][next_grid_position[0]]
		except Exception: 
			next_ent = False
		
		# print(type(next_ent))
		# print(self.grid_position_record)

		if next_ent:
			#code for collision
			if next_ent[0] == "Apple":
				#destroy apple 
				apple = next_ent[1]
				apple.rectangle.undraw()
				#do not remove previous snake square
				#the next snake square will be update after the if block
				#the entity list will also be updated
				#update length variable and score
				self.length += 1
				self.score += 50

				#move
				#grid coords
				# new_grid_coords = [next_grid_position[0], next_grid_position[1]]
				#concatenate lists
				print(self.grid_position_record, "\t", next_grid_position)
				self.grid_position_record = add_nested_list_to_front(next_grid_position, self.grid_position_record)
				#rectangle save
				new_head = graphics_handler.draw_square_from_grid(win, next_grid_position, self.color)
				self.rectangle_record = add_nested_list_to_front(new_head, self.rectangle_record)
				#update ent list 
				ent_grid[new_grid_coords[1]][new_grid_coords[0]] = ["Snake", new_head]

				return ent_grid


		else:
			#no collision, will move, delete last square to maintain length
			rectangle_to_teardown = self.rectangle_record.pop()
			p1 = rectangle_to_teardown.getP1()
			p1x, p1y = int(p1.getX()), int(p1.getY()) 
			[g1x, g1y] = graphics_handler.coords_to_grid(p1x, p1y)
			#remove from entlist
			ent_grid[g1y][g1x] = False
			#remove from grids coords list
			# self.grid_position_record.pop()
			#undraw
			rectangle_to_teardown.undraw()
			#move
			#grid coords
			# new_grid_coords = [next_grid_position[0], next_grid_position[1]]

			print(self.grid_position_record, "\t", next_grid_position)
			#concatenate lists
			self.grid_position_record = add_nested_list_to_front(next_grid_position, self.grid_position_record)
			# print(self.grid_position_record)
			#rectangle save
			new_head = graphics_handler.draw_square_from_grid(win, next_grid_position, self.color)
			self.rectangle_record = add_nested_list_to_front(new_head, self.rectangle_record)
			#update ent list 
			ent_grid[new_grid_coords[1]][new_grid_coords[0]] = ["Snake", new_head]

			return ent_grid

		




class Apple(object):
	"""The primary method of gaining score. 
	
	Eating an apple should increase snake length and increase score."""
	ent_type = "Apple" #it's casting to Rectangle
	grid_position = []
	#store rectangle
	rectangle = False

	def __init__(self, win, occupied_spaces, color="red"):
		"""constructor"""
		# Get an unused position
		guess = graphics_handler.get_random_grid(win)
		while guess in occupied_spaces:
			guess = graphics_handler.get_random_grid(win)

		# Customize and draw apple
		self.grid_position = guess
		self.rectangle = graphics_handler.draw_square_from_grid(win, guess, color)
		# print(type(apple))


def add_to_entity_list(obj, ent_grid, x, y, tag):
	""""A list of every gridspace, with the information of a string tag and the object"""
	ent_grid[y][x] = [tag, obj]
	return ent_grid

def add_nested_list_to_front(new_top_list, list_of_lists):
	new_list_of_lists = []
	new_list_of_lists.append(False)
	new_list_of_lists[0] = new_top_list
	for index in range(1, len(list_of_lists)):
		new_list_of_lists.append(False)
		new_list_of_lists[index] = list_of_lists[index-1]

	return new_list_of_lists
