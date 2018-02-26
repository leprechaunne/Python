###########################################
###########################################
###########################################
class Scene(object):

	def enter(self):
		print(f"{self} has not yet been implemented.")
		exit(1)

###########################################
###########################################
###########################################
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene - self.scene_map.next_scene(next_scene_name)

		#print last
		current_scene.enter()

###########################################
class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your Mom would be proud... if she were smarter.",
		"Git gud.",
		"I have a small puppy that's better at this.",
		"You're worse than your Dad's jokes."
	]

	def enter(self):
		print(Death.quips[randint(0, len(self.quips)-1)])
		exit(1)

###########################################
class CentralCorridor(Scene):

	def enter(self):
		print(dedent("""
			The Gothons of Planet Percal #25 have invaded your ship and
			destroyed your entire crew. You are the last surviving 
			member and your last mission is to get the neutron destroyer
			bomb from the Weapons Armory, put it in the bridge, and
			blow the ship up after getting into an escape pod.

			You're running down the central corridor to the Weapons
			Armory when a Gothon jumps out, red scaly skin, dark grimy 
			teeth, and evil clow costume flowing around his hate-
			filled body. He's blocking the door to the Armory and
			about to pull a weapon to blast you.
			"""))

		action = input("> ")

		if any(match in [""])

###########################################
class TheBridge(Scene):

	def enter(self):
		pass

###########################################
class EscapePod(Scene):
	def enter(self):
		pass

#######################################
###########################################
###########################################
class Map(object):
	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass

	def opening_scene(self):
		pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()