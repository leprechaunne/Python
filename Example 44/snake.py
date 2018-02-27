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
		if k in valid_inputs:
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
		k = getKey()
		if k in valid_inputs:
			if k in ['w', 'Up']:
				snake.direction = 'north'
			elif k in ['s', 'Down']:
				snake.direction = 'south'
			elif k in ['a', 'Left']:
				snake.direction = 'west'
			elif k in ['d', 'Right']:
				snake.direction = 'east'




		p1 = win.getMouse()
		print(p1)


		#TODO change
		refresh_rate = 1 #second
		sleep(refresh_rate) #sleep for current delay, starting at 1 sec

	win.close()




#TODO - implement points and high scores
#def draw_title_screen(win, points, high_scores):
# @accepts(graphics.GraphWin) find a way to force input Type
def draw_title_screen(win):
	title = Text(Point(250, 175), "SNAKE")
	title.setSize(36)
	title.setTextColor("white")


	subtitle = Text(Point(250,175+36), "PRESS WASD OR ARROW KEYS TO CONTINUE")
	subtitle.setSize(10)
	subtitle.setTextColor("white")
	return title, subtitle

main()