from graphics import *
from random import *

class Snake:
	#direction the snake is moving
	direction = "north"
	#current position of the HEAD of the snake
	head_position = {
		'x' : 25, 
		'y' : 25
		} #each square in the grid is 10px X 10px, so to get the coordinates, position*10
	#how "long" the snake is
	snake_length = 1
	#array of all positions (it is a stack, in the way that the last piece is always the only one 
	#	that needs to be redrawn)
	position_record = [[25, 25]]
	#keeping track of score
	score = 0

	def __init__(self, win):
		#initialize
		####simply a reference variable
		DIRECTIONS = ["north", "south", "east", "west"]
		self.direction = DIRECTIONS[randint(0, 3)]
		head_position = [25, 25]
		snake_length = 1
		position_record = [head_position]
		#TODO: speed setting
		score = 0
		self.draw_next_position(win)

	def draw_next_position(self, win):
		#the grid is 50 x 50 with each section being a 10 x 10 square
		#furthermore, each section of the snake is only 8 x 8 but this is achieved with outlines
		previous_square = self.head_position
		direction = self.direction
		#initializing next square at base point
		next_square = previous_square
		#modifying position by direction
		if "north" == direction:
			next_square['y'] -=  1
		elif "south" == direction:
			next_square['y'] += 1
		elif "east" == direction:
			next_square['x'] +=1
		elif "west" == direction:
			next_square['x'] -= 1

		next_rect_x_1 = next_square['x'] * 10 #find coords and shrink rect by 1
		next_rect_x_2 = next_rect_x_1 + 9
		next_rect_y_1 = next_square['y'] * 10# ^ ^ ^
		next_rect_y_2 = next_rect_y_1 + 9

		print(f"{next_rect_x_1}, {next_rect_y_1}:\t{direction}")
		corner1 = Point(next_rect_x_1, next_rect_y_1)
		corner2 = Point(next_rect_x_2, next_rect_y_2)
		next_rect = Rectangle(corner1, corner2)
		next_rect.setWidth(1)
		# next_rect.setOutline("red")
		next_rect.setFill("white")
		next_rect.draw(win)	                                                    






