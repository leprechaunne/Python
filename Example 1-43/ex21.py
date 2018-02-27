def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b

#output
print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#A 'puzzle'
print("\nHere's a puzzle:")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# age + (height - (weight * (iq/2)))
# age + (height - (weight * 25))
# age + (height - (180 * 25))
# age + (74  - 4500)
# 35 + -4,426
# -4,391

print("That becomes: ", what, "Can you do it by hand?")