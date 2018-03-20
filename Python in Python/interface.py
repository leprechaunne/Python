from graphics import *
import settings

#-----------------------------------------------------------
#			Misc Functions
#-----------------------------------------------------------

def wait_for_key(acceptable_key_array):
	key_pressed = ''

	while not key_pressed in acceptable_key_array:
		key_pressed = settings.win.checkKey()

#----------------------------------------------------------
#			Graphics functions. Likely to be moved
#----------------------------------------------------------

def run_title_screen():
	#title
	##################################################
	title_anchor = ((settings.grid_cells_per_side / 2))
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


	title.draw(settings.win)
	subtitle.draw(settings.win)
	wait_for_key(['Return'])

def teardown_window():
	item_list_length = len(settings.win.items)
	for i in range(item_list_length):
		settings.win.items[0].undraw()
