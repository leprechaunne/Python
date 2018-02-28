from graphics import *
from Snake_Engine import *
from time import sleep
import winsound
	#frequency
	#duration
	#winsound.Beep(hz, length)
valid_inputs = ['w', 'a', 's', 'd', "Up", "Left", "Down", "Right"]

def main():
	#create game window
	win = GraphWin("Snake", 500, 500)
	win.setBackground("black")

	#								title screen
	#-----------------------------------------------------------------------
	title, subtitle = draw_title_screen(win)
	title.draw(win)
	subtitle.draw(win)
	#await input
	flag = False
	while not flag:
		k = win.getKey()
		# print(k)
		if k in 'Return':
			flag = True

	#								game play
	#----------------------------------------------------------------------
	#get rid of title elements
	title.undraw()
	subtitle.undraw()

	#draw boundary
	corner1 = Point(11, 11)
	corner2 = Point(489, 489)
	out_of_bounds = Rectangle(corner1, corner2)
	out_of_bounds.setWidth(1)
	out_of_bounds.setOutline("white")
	out_of_bounds.draw(win)

	#############################################
	############	Actual Game 	#############
	#############################################
	snake = Snake(win)
	
	iteration_count = 0
	while True:
		#track time (use of timer not implemented)
		iteration_count += 1

		#check for valid input
		k = win.checkKey()
		if k in valid_inputs:
			if k in ['w', 'Up']:
				snake.direction = 'north'
			elif k in ['s', 'Down']:
				snake.direction = 'south'
			elif k in ['a', 'Left']:
				snake.direction = 'west'
			elif k in ['d', 'Right']:
				snake.direction = 'east'

		#draw
		snake.draw_next_position(win)
			
		snake.remove_last_position(win)


		#TODO change
		refresh_rate = .5 #second
		sleep(refresh_rate) #sleep for current delay, starting at 1 sec
		# print(f"Tick {iteration_count}.")

	win.close()




#TODO - implement points and high scores
#def draw_title_screen(win, points, high_scores):
# @accepts(graphics.GraphWin) find a way to force input Type
def draw_title_screen(win):
	title = Text(Point(250, 175), "SNAKE")
	title.setSize(36)
	title.setTextColor("white")


	subtitle = Text(Point(250,175+36), "PRESS ENTER TO CONTINUE")
	subtitle.setSize(10)
	subtitle.setTextColor("white")
	return title, subtitle

#this is to better see the grid and is for testing purposes only
#may be used for aesthetics later
def draw_grid(win):
	for x in range(0, 49, 2):
		for y in range(0, 49, 2):
			p1 = Point(x * 10, y * 10)
			p2 = Point(x * 10 + 9, y * 10 + 9)
			tile = Rectangle(p1, p2)
			tile.setWidth(0)
			tile.setFill("cornsilk4")
			# tile.setOutline("cornsilk4")
			tile.draw(win)
		#end y
	#end x





main()
