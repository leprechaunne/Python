"""The master file, organizes game into 3 sections and uses the other files to perform subroutines"""
import graphics_handler, entities, graphics
from time import sleep
from random import randint

################	Constants

#acceptable_input are the controls defined by a dictionary
#for things like controllers, install necessary packages and add them in the appropriate array
acceptable_input = {
					'move_up': ['Up', 'w'],
					'move_down': ['Down', 's'],
					'move_left': ['Left', 'a'],
					'move_right': ['Right', 'd']
					}

tick_speed = .5 #seconds. This should be modified by difficulty, and increment

###############		Main method
def main():
	""" The largest scope function, routes to subsections """
	# Build a window with graphics.py
	win = graphics_handler.create_window()
	# Build title screen (it will automatically teardown)
	graphics_handler.generate_title_screen(win)
	# Once the user presses enter, build game board
	graphics_handler.generate_game_board(win)
	#building grid 2d list to hand to entities for optimized collision detection
	entity_list = graphics_handler.create_entity_list(win)

	#CODE TO READ INPUT AND ALTER SNAKE AND BOARD
	#build snake(s)
	player1 = entities.Snake(win)
	apple = entities.Apple(win, player1.grid_position_record)
	entities.add_to_entity_list(apple, entity_list, apple.grid_position[0], apple.grid_position[1], "Apple")

	game_over = False
	ticks_passed = 0
	while not game_over:
		#check for valid input
		k = win.checkKey()
		current_direction = player1.direction

		#change direction if it's not a 180 and the user input a direction
		# print(k)
		if (k in acceptable_input['move_up']) and (current_direction != entities.DIRECTION_DOWN):
			player1.direction = entities.DIRECTION_UP
		elif (k in acceptable_input['move_down']) and (current_direction != entities.DIRECTION_UP):
			player1.direction = entities.DIRECTION_DOWN
		elif (k in acceptable_input['move_left']) and (current_direction != entities.DIRECTION_RIGHT):
			player1.direction = entities.DIRECTION_LEFT
		elif (k in acceptable_input['move_right']) and (current_direction != entities.DIRECTION_LEFT):
			player1.direction = entities.DIRECTION_RIGHT

		#Proceeding after input handled
		# print(ticks_passed, ":\t", player1.direction)
		entity_list = player1.move_direction(win, entity_list)
		###############################################################################
		##############################################################################
		#					DO NOT FORGET TO RETURN MODIFIED ENTITY LIST
		
		# give a score point for not dying
		player1.score += 1

		sleep(tick_speed)

		#update tick number
		ticks_passed += 1
		print(ticks_passed)

	#Teardown 
	graphics_handler.teardown_all(win)
	



	#handle restart
	############if restart:
	############	main() #recurrsion
	############	win.close()
	############	quit() #no matter how many restarts occur, the first exception with trigger quit()

main()
#That's all, folks!