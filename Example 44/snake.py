from graphics import *
from Snake_Engine import *
from time import sleep
from random import randint
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
	#spawn snake
	snake = Snake(win)
	#spawn first apple 
	current_apple = spawn_apple(win, snake)
	apple_eaten = False

	# initialize
	iteration_count = 0
	score = 0

	#game loop
	while True:
		#track time (use of timer not implemented)
		iteration_count += 1

		#check for valid input
		k = win.checkKey()
		current_direction = snake.direction
		#apply direction change if prompted and valid
		if k in valid_inputs:
			if (k in ['w', 'Up']) and (current_direction != "south"):
				snake.direction = 'north'
			elif (k in ['s', 'Down']) and (current_direction != "north"):
				snake.direction = 'south'
			elif (k in ['a', 'Left']) and (current_direction != "east"):
				snake.direction = 'west'
			elif (k in ['d', 'Right']) and (current_direction != "west"):
				snake.direction = 'east'

		#draw
		snake.draw_next_position(win)

		#apple generation or capture

		if is_rectangle_equal(current_apple, snake.position_record[0]):
			print("he eated it")
			# snake.add_square(win)
		else:
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

# #this is to better see the grid and is for testing purposes only
# #may be used for aesthetics later
# def draw_grid(win):
# 	for x in range(0, 49, 2):
# 		for y in range(0, 49, 2):
# 			p1 = Point(x * 5, y * 5)
# 			p2 = Point(x * 5 + 9, y * 5 + 9)
# 			tile = Rectangle(p1, p2)
# 			tile.setWidth(0)
# 			tile.setFill("cornsilk4")
# 			# tile.setOutline("cornsilk4")
# 			tile.draw(win)
# 		#end y
# 	#end x

def spawn_apple(win, snake):
	#must find an unoccupied space to spawn an apple
	apple_spawned = False

	while not apple_spawned:
		#generate a random point
		apple_guess_1 = Point(randint(1, 49)*10, randint(1, 49)*10)
		apple_guess_2 = Point(apple_guess_1.x + 9, apple_guess_1.y + 9)
		apple_guess = Rectangle(apple_guess_1, apple_guess_2)

		#check if apple is where any segment of the snake is
		if not (apple_guess in snake.position_record):
			apple_spawned = True

			apple_guess.setWidth(1)
			apple_guess.setOutline("black")
			apple_guess.setFill("red")

			apple_guess.draw(win)
			return apple_guess

		#end of apple succeeded
	#end of apple loop


def is_rectangle_equal(rect1, rect2):
	 return (rect1.p1 == rect2.p1) and (rect1.p2 == rect2.p2)




main()
