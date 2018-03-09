def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"\tYou have {cheese_count} cheeses!")
	print(f"\tYou have {boxes_of_crackers} boxes of crackers!")
	print(f"\tMan that's enough for a party!")
	print("\tGet a blanket\n")

#constants
amount_of_cheese = 10
amount_of_crackers = 50

#printing
print("We can just give the funciton numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from out script")
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#jeez, I wish he would use 'num' instead of these ridiculously long variable names

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)