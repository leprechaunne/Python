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

###############		Main method
def main():
	""" The largest scope function, routes to subsections """
	# Build a window with graphics.py
	win = graphics_handler.create_window()
	# Build title screen (it will automatically teardown)
	graphics_handler.generate_title_screen(win)
	# Once the user presses enter, build game board
	graphics_handler.generate_game_board(win)

	#CODE TO READ INPUT AND ALTER SNAKE AND BOARD
	#build snake(s)
	player1 = entities.Snake(win)
	first_apple = entities.Apple(win, player1.position_record)


	while True:
		pass

	#Teardown 
	graphics_handler.teardown_all(win)
	



	#handle restart
	############if restart:
	############	main() #recurrsion
	############	win.close()
	############	quit() #no matter how many restarts occur, the first exception with trigger quit()

main()
#That's all, folks!