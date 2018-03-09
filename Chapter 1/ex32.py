count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#first style of for loop
for number in count:
	print(f"This is count {number}")

#same as above
for fruit in fruits:
	print(f"A fruit of type: {fruit}")

#for loops can also go thru lists with multiple data types
#notice we have to use {} since we dont know what's in it
for i in change:
	print(f"I got {i}")

#we can also build lists, first start with an empty one
elements = []

for i in range(0, 6):
	print(f"Adding {i} to the list.")
	#append the value
	elements.append(i)

#now we can print them out too
for i in elements:
	print(f"Element was: {i}")