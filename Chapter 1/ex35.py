# I've started taking liberties to deviate from the book for ineffective code

import sys
import os

def prompt(msg):
	os.system('cls')
	print(msg)

def gold_room():
	prompt("This room is full of gold. How much do you take?")

	choice = input("> ")
	try:
		how_much = int(choice)
	except ValueError:
		dead("Man, learn to type a number.")

	if how_much < 50:
		prompt("Nice, you're not greedy, you win!")
		sys.exit(0)
	else:
		dead("You greedy bastard!")

def bear_room():
	
	bear_moved = False

	while True:
		prompt("""There is a bear here.\nThe bear has a bunch of honey.""")
		if not bear_moved:
			print("""The fat bear is in front of another door.\nHow are you going to move the bear?""")
		else:
			print("The bear has moved.")

		choice = input("> ")
		choice = choice.lower()

		if choice == "take honey":
			dead("The bear looks at you and then slaps your face off.")
		elif "taunt" in choice and "bear" in choice and not bear_moved:
			prompt("""The bear moved from the door.\nYou can go through it now.""")
			bear_moved = True
		elif "taunt" in choice and "bear" in choice and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif "open" in choice and "door" in choice and not bear_moved:
			prompt("There is a bear in the way.")
		elif "open" in choice and "door" in choice and bear_moved:
			gold_room()
		else:
			prompt("I got no idea what that means.")

def cthulhu_room():
	prompt("""Here you see the great evil Cthulhu.\nHe, it, whatever stares at you and you go insane.\nDo you flee for you life or eat your head?""")

	choice = input("> ")
	choice = choice.lower()

	if "flee" in choice:
		start()
	elif "head in choice":
		dead("Well that was tasty!")
	else:
		dead("The might Cthulhu angers at your indecisiveness and consumes your life essence.")

def dead(why):
	prompt(f"{why}\nGood job!")
	sys.exit(0)

def start():
	prompt("""You are in a dark room.\nThere is a door to your right and left.\nWhich one do you take?""")

	choice = input("> ")
	choice = choice.lower()

	if "left" in choice:
		bear_room()
	elif "right" in choice:
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")

start()