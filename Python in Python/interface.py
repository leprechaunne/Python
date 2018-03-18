from graphics import *
from math import floor

#-----------------------------------------------------------
#			Misc Functions
#-----------------------------------------------------------

def wait_for_key(win, acceptable_key_array):
	key_pressed = ''

	while not key_pressed in acceptable_key_array:
		key_pressed = win.checkKey()

#----------------------------------------------------------
#			Graphics functions. Likely to be moved
#----------------------------------------------------------

def run_title_screen(win, new_coords):
	#title
	##################################################
	title_anchor = ((new_coords / 2))
	title_anchor_x, title_anchor_y = title_anchor, title_anchor + 1 #anchored in center
	# title_anchor = Point(win.)
	title = Text(Point(title_anchor_x, title_anchor_y), "Python in Python")
	title.setTextColor("white")
	title.setSize(36)


	#subtitle
	##################################################
	subtitle_anchor_x, subtitle_anchor_y = title_anchor_x, title_anchor_y -1
	#create text object
	subtitle = Text(Point(subtitle_anchor_x, subtitle_anchor_y), "PRESS ENTER TO CONTINUE")
	subtitle.setTextColor("white")
	subtitle.setSize(12)


	title.draw(win)
	subtitle.draw(win)
	wait_for_key(win, ['Return'])

def teardown_window(win):
	for graphics_object in win.items:
		graphics_object.undraw()
