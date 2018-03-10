##lexicon is essentially an abstract class, its references will be used more like
##tools than an instanced object
##for this reason, the scope of the all objects will be global in the file lexicon

## constants
directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stops = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']

## functions
def scan(raw_input):
	#make sure nil doesn't throw an exception error
	if not raw_input:
		return ""

	#convert to lsit
	##cooked_input = raw_input.lower().split()
	#assert_equal is case sensitive
	cooked_input = raw_input.split()

	#formatting each entry to have class types and adding them to the final return
	return_value = []

	for word in cooked_input:
		if word in directions:
			return_value.append(('direction', word))
		elif word in verbs:
			return_value.append(('verb', word))
		elif word in stops:
			return_value.append(('stop', word))
		elif word in nouns:
			return_value.append(('noun', word))
		elif isa_number(word):
			return_value.append(('number', isa_number(word)))
		else:
			return_value.append(('error', word))

	return return_value


	
def isa_number(word):
	try:
		number = int(word)
		if number < 10**9:
			return number
		else:
			return False
	except ValueError:
		return False
