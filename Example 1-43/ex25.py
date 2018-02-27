def breakWords(str):
	"""This function will break up words for us."""
	words = str.split(' ')
	return words

def sortWords(words):
	"""Sorts the words."""
	return sorted(words)

def printFirstWord(words):
	"""Prints the first word affer 'popping' it off; this indicates that the list is a queue and not a stack"""
	word = words.pop(0)
	print(word)

def printLastWord(words):
	"""prints the last word after popping it off"""
	word = words.pop(-1)
	print(word)

def  sortSentence(sentence):
	"""Takes in a full sentence and returns the sorted words"""
	words = breakWords(sentence)
	return sortWords(words)

def printFirstLast(sentence):
	words = breakWords(sentence)
	printFirstWord(words)
	printLastWord(words)

def printFirstLastSorted(sentence):
	words = sortSentence(sentence)
	printFirstWord(words)
	printLastWord(words)
