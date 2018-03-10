from sys import argv

script, input_file = argv

#functions
def print_all(f):
	print(f.read())

def rewind(f):
	f.seek(0)

def println(numLine, f):
	print(f"{numLine})", f.readline())


#printing
current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)
print("Now let's rewind to the beginning of the file.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
println(current_line, current_file)
current_line += 1
println(current_line, current_file)
current_line += 1
println(current_line, current_file)