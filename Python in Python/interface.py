from graphics import *
import settings
import sys

#-----------------------------------------------------------
#			Misc Functions
#-----------------------------------------------------------

def wait_for_key(acceptable_key_array):
	key_pressed = ''

	while not key_pressed in acceptable_key_array:
		key_pressed = settings.win.checkKey()

	return key_pressed

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
	title.setSize(24)


	#subtitle
	##################################################
	subtitle_anchor_x, subtitle_anchor_y = title_anchor_x, title_anchor_y - 4
	#create text object
	subtitle = Text(Point(subtitle_anchor_x, subtitle_anchor_y), "PRESS ENTER TO CONTINUE")
	subtitle.setTextColor("white")
	subtitle.setSize(8)


	title.draw(settings.win)
	subtitle.draw(settings.win)
	wait_for_key(['Return'])

def setup_game_board():
	p1 = settings.grid_cells_per_side - 1
	p2 = settings.grid_cells_per_side - 3
	border = Rectangle(Point(1,1), Point(p1, p2))
	border.setWidth(1)
	border.setOutline("white")
	border.draw(settings.win)


def teardown_window():
	item_list_length = len(settings.win.items)
	for i in range(item_list_length):
		settings.win.items[0].undraw()




def test_grid():
	white = True

	for y in range(settings.grid_cells_per_side):
		white = not white
		for x in range(settings.grid_cells_per_side):
			if white:
				rect = Rectangle(Point(y,x), Point(y+1,x+1))
				rect.setFill("#DF7D1E")
				rect.draw(settings.win)

			white = not white


def game_over(loss_reason):
	# print(f"You lose: {loss_reason}")
	teardown_window()
	#gameover
	##################################################
	game_over_anchor = ((settings.grid_cells_per_side / 2))
	game_over_anchor_x, game_over_anchor_y = game_over_anchor, game_over_anchor + 1 #anchored in center
	# game_over_anchor = Point(win.)
	game_over = Text(Point(game_over_anchor_x, game_over_anchor_y), "GAME OVER")
	game_over.setTextColor("white")
	game_over.setSize(24)


	#reason
	##################################################
	reason_anchor_x, reason_anchor_y = game_over_anchor_x, game_over_anchor_y - 4
	#create text object	
	if loss_reason == "OOB":
		reason_text = "You died by running into the wall."
	elif loss_reason == "COLLISION":
		reason_text = "You died by eating yourself."
	else:
		reason_text = "You died."

	reason = Text(Point(reason_anchor_x, reason_anchor_y), f"{reason_text}")
	reason.setTextColor("white")
	reason.setSize(8)

	#recycled subtitle code
	title_anchor = ((settings.grid_cells_per_side / 2))
	title_anchor_x, title_anchor_y = title_anchor, title_anchor #anchored in center
	subtitle_anchor_x, subtitle_anchor_y = title_anchor_x, title_anchor_y - 5
	subtitle = Text(Point(subtitle_anchor_x, subtitle_anchor_y), "PRESS ENTER TO RESTART")
	subtitle.setTextColor("white")
	subtitle.setSize(8)

	#recycled subtitle code
	# title_anchor = ((settings.grid_cells_per_side / 2))
	# title_anchor_x, title_anchor_y = title_anchor, title_anchor #anchored in center
	subtitle2_anchor_x, subtitle2_anchor_y = title_anchor_x, title_anchor_y - 6
	subtitle2 = Text(Point(subtitle2_anchor_x, subtitle2_anchor_y), "PRESS ESCAPE TO QUIT")
	subtitle2.setTextColor("white")
	subtitle2.setSize(8)

	game_over.draw(settings.win)
	reason.draw(settings.win)
	subtitle.draw(settings.win)
	subtitle2.draw(settings.win)

	selection = wait_for_key(['Return', 'Escape'])

	if selection == 'Return':
		python.main()
	else:
		sys.exit()
