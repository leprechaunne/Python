from graphics import *
import winsound
	#frequency
	#duration
	#winsound.Beep(hz, length)

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
		if k in ['w', 'a', 's', 'd', "Up", "Left", "Down", "Right"]:
			flag = True

	#								game play
	#----------------------------------------------------------------------
	#get rid of title elements
	title.undraw()
	subtitle.undraw()





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