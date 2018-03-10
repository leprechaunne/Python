from graphics import *
from random import *




class Snake:
	#direction the snake is moving
	direction = "north"
	#current position of the HEAD of the snake
	head_position = [25, 25] #each square in the grid is 10px X 10px, so to get the coordinates, position*10
	#how "long" the snake is
	snake_length = 1
	#array of all positions (it is a stack, in the way that the last piece is always the only one 
	#	that needs to be redrawn)
	position_record = []


	def __init__(self, win):
		#initialize
		####simply a reference variable
		DIRECTIONS = ["north", "south", "east", "west"]
		self.direction = DIRECTIONS[randint(0, 3)]
		self.head_position = [25, 25]
		self.snake_length = 1
		#TODO: speed setting
		self.draw_next_position(win)

	def draw_next_position(self, win):
		#the grid is 50 x 50 with each section being a 10 x 10 square
		#furthermore, each section of the snake is only 8 x 8 but this is achieved with outlines
		# next_square = self.head_position
		direction = self.direction

		#modifying position by direction
		if "north" == direction:
			# next_square[1] -=  1
			self.head_position[1] -= 1
		elif "south" == direction:
			# next_square[1] += 1
			self.head_position[1] += 1
		elif "east" == direction:
			# next_square[0] +=1
			self.head_position[0] += 1
		elif "west" == direction:
			# next_square[0] -= 1
			self.head_position[0] -= 1

		next_rect_x_1 = self.head_position[0] * 10 #find coords and shrink rect by 1
		next_rect_x_2 = next_rect_x_1 + 9
		next_rect_y_1 = self.head_position[1] * 10# ^ ^ ^
		next_rect_y_2 = next_rect_y_1 + 9

		# #####################print(f"{next_rect_x_1}, {next_rect_y_1}:\t{direction}")
		corner1 = Point(next_rect_x_1, next_rect_y_1)
		corner2 = Point(next_rect_x_2, next_rect_y_2)
		next_rect = Rectangle(corner1, corner2)
		next_rect.setWidth(1)
		next_rect.setFill("white")
		self.position_record.append(next_rect)
		# print(self.position_record)
		next_rect.draw(win)	
		# print("|")
		# print('|', end=' ', flush=True)
		                                                    
		#

	def remove_last_position(self, win):
		remove_from_snake = self.position_record.pop(0)
		remove_from_snake.undraw()


	def add_square(win):
		self.snake_length += 1
		self.position_record.append()
