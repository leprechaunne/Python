#get my ()wers
with open("ex27.txt") as f:
	lines = f.read().splitlines()
#initialize score
score = 0

def toBoolean(str, num):
	if str.lower() == "true":
		return True
	else:
		return False
question = 1

if(toBoolean(lines.pop(0), question) == True and True):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == False and True):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (1 == 1 and 2 == 1)):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == ("test" == "test")):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (1 == 1 or 2 != 1)):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (True and 1 == 1)):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (False and 0 != 0)):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (True or 1 == 1)):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == ("test" == "testing")):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (1 != 0 and 2 == 1)):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == ("test" != "testing")):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == ("test" == 1)):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (not (True and False))):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (not(1 == 1 and 0 != 1))):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (not(10 == 1 or 1000 == 1000))):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (not( 1 != 10 or 3 == 4))):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == ("testing" == "testing" and "Zed" == "Cool Guy")):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (1 == 1 and not("testing" == 1 or 1 == 0))):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == ("chunky" == "bacon" and not(3 == 4 or 3 == 3))):
	score += 1
	question += 1
if(toBoolean(lines.pop(0), question) == (3 == 3 and not("testing" == "testing" or "Python" == "Fun"))):
	score += 1
	question += 1

print(score / 20 * 100, "%")