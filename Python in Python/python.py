""" This is just a snake program in a scripting language.

More of a test of ability for large projects than anything."""
import settings
from graphics import *
from interface import *
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
	while not game_over:
		key_pressed = settings.win.checkKey()

		#evaluate input
		x_mod, y_mod = 0, 0

		if key_pressed in settings.input_dictionary["up"]:
			y_mod = 1
		elif key_pressed in settings.input_dictionary["down"]:
			y_mod = -1
		elif key_pressed in settings.input_dictionary["right"]:
			x_mod = 1
		elif key_pressed in settings.input_dictionary["left"]:
			x_mod = -1

		
		# game_over = True
		sleep(settings.tick_length)

	#if repeat:
	#	main()
	#else:
	#	exit()




main()