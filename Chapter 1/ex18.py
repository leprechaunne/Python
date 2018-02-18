# this one is like the argv scripts
def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

#this time, without using the variable number of args parameter
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# and a single parameter for good measure
def print_one(arg1):
	print(f"arg1: {arg1}")

# no args
def print_none():
	print("I got nothin'.")


#use functions
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()