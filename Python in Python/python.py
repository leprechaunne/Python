""" This is just a snake program in a scripting language.

More of a test of ability for large projects than anything."""
import settings
from graphics import *
from interface import *
from objects import *
from time import sleep

# Frequently used objects (such as the game window) and
# Constants that alter gameplay have been moved to
# settings.py to greatly reduce the amount of parameters passing
# thus (hopefully) removing much of the wasted RAM allocation

def main():
	settings.init()


	run_title_screen()
	#waits for enter press, then teardown
	# print(settings.win.items, "\n\n\n\n\n\n")
	teardown_window()

	#####################################################
	#					Gameplay Loop					#
	#####################################################
	# print(type(not game_over))

	game_over = False
	# test_grid()
	player_one = Snake()

	while not game_over:
		key_pressed = settings.win.checkKey()

		#evaluate input
		delta_x, delta_y = 0, 0

		if key_pressed in settings.input_dictionary["up"]:
			player_one.direction = player_one.direction_dict["up"]
		elif key_pressed in settings.input_dictionary["down"]:
			player_one.direction = player_one.direction_dict["down"]
		elif key_pressed in settings.input_dictionary["left"]:
			player_one.direction = player_one.direction_dict["left"]
		elif key_pressed in settings.input_dictionary["right"]:
			player_one.direction = player_one.direction_dict["right"]

		player_one.move()
		
		# game_over = True
		sleep(settings.tick_length)

	#if repeat:
	#	main()
	#else:
	#	exit()




main()