from math import floor
from random import randint
from graphics import *
from interface import *
from collections import deque
import settings



class Coordinate():
	""" Simple storage of x,y coordinates to simplify position records"""
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Apple():
	""" Simple red square that the snake wants to eat"""
	def __init__(self, override=False, color="red"):
		if not override:
			#find empty space
			test_coords = [randint(1, settings.grid_cells_per_side - 2), randint(1, settings.grid_cells_per_side - 4)]
			while settings.entity_grid[test_coords[1]][test_coords[0]]:
				test_coords = [randint(1, settings.grid_cells_per_side - 2), randint(1, settings.grid_cells_per_side - 4)]

			coords = Coordinate(test_coords[0], test_coords[1])

			p1 = Point(coords.x, coords.y)
			p2 = Point(p1.getX() + 1, p1.getY() + 1)
			apple = Rectangle(p1, p2)
			apple.setFill(color)
			apple.draw(settings.win)
			self.rectangle = apple
			settings.entity_grid[coords.y][coords.x] = self



class Snake():
	"""User controlled object that consists of squares.
	
	Color can be passed with Snake(color)
	Snake's main properties are its location_list, length, and score."""

	# color 				- the color of the blocks drawn by the snake
	# length 				- how many blocks the snake is made of
	# score					- each snake is applied one-per-player, so the easiest mode of storage is in snake
	# grid_position_record	- queue of grid coords
	# position_record 		- use this file's Coordinate class 
	#if the directions become heavily used, you can make a dictionary to go from
		#number to its corollary constant

	direction_dict = {
		"up": 0,
		"right": 1,
		"down": 2,
		"left": 3
	}



	class SnakeSegment():

		def __init__(self, x, y, color="green", override=False):
			if not override:
				self.x = x
				self.y = y
				#draw first square
				p1 = Point(x, y)
				p2 = Point(p1.getX() + 1, p1.getY() + 1)
				head = Rectangle(p1, p2)
				head.setFill(color)
				head.setOutline("black")
				head.setWidth(1)


				head.draw(settings.win)
				self.rectangle = head
				settings.entity_grid[y][x] = self

		
	def __init__(self, color="green"):
		self.color = color
		self.length = 1
		self.score = 0
		self.direction = randint(0,3)
		#spawn in middle of grid
		middle_square = floor(settings.grid_cells_per_side / 2)
		middle_coord = Coordinate(middle_square, middle_square)
		self.grid_position_record = deque([middle_coord])
		self.head_position = middle_coord
		settings.entity_grid[middle_square][middle_square] = self.SnakeSegment(middle_square, middle_square, self.color)


	def move(self):
		delta_x, delta_y = 0, 0

		# print(self.direction)

		if self.direction == self.direction_dict["up"]:
			delta_y = 1
			#print("moving")
		elif self.direction == self.direction_dict["down"]:
			delta_y = -1
			#print("moving")
		elif self.direction == self.direction_dict["left"]:
			delta_x = -1
			#print("moving")
		elif self.direction == self.direction_dict["right"]:
			delta_x = 1
			#print("moving")

		x = self.head_position.x
		y = self.head_position.y
		next_x = x + delta_x
		next_y = y + delta_y

		x_fail = not (next_x in range(settings.play_area_lower_left[0], settings.play_area_upper_right[0]))
		y_fail = not (next_y in range(settings.play_area_lower_left[1], settings.play_area_upper_right[1] - 2))

		if x_fail or y_fail:
			game_over("OOB")

		try:
			collision = type(settings.entity_grid[next_y][next_x]) #this fails if a snake segment touches another
		except Exception:
			game_over("LEFT SCREEN")
		# print(collision)
		# print(f"[{x},{y}], [{next_x}, {next_y}]")


		if collision == type(False):
			# print(type(settings.entity_grid[y][x]))
			try:
				#undraw FURTHEST segment
				tail_end = self.grid_position_record.pop()
				settings.entity_grid[tail_end.y][tail_end.x].rectangle.undraw()
				settings.entity_grid[tail_end.y][tail_end.x] = False #old spot is removed
			except Exception:
				print(Exception)

			#draw new segment and replace
			new_head = self.SnakeSegment(next_x, next_y)
			position = Coordinate(next_x, next_y)
			self.head_position = position
			#replace last one
			self.grid_position_record.appendleft(position)		#put one on left
		elif collision == type(Apple(override=True)):
			# print("APPLE!!!!")
			try:
				#undraw apple
				settings.entity_grid[next_y][next_x].rectangle.undraw()
				pass
			except Exception:
				print(Exception)
			# settings.entity_grid[y][x] = False

			#replace apple with snake
			head = self.SnakeSegment(next_x, next_y, self.color)
			self.head_position = head
			self.grid_position_record.appendleft(head)
			#add 2 more apples
			# new_tail_1 = self.SnakeSegment(x - delta_x, y - delta_y, self.color)
			# # self.head_position = new_tail_1
			# self.grid_position_record.append(new_tail_1)

			# new_tail_2 = self.SnakeSegment(x - (delta_x * 2), y - (delta_y * 2), self.color)
			# # self.head_position = new_tail_2
			# self.grid_position_record.append(new_tail_2)

			apple = Apple()

			settings.tick_length *= .75
		elif collision == type(Snake.SnakeSegment(0,0,override=True)):
				game_over("COLLISION")

