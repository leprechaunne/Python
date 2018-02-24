#given variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
#calculations
##cars that cannot be driven due to amount of drivers
cars_not_driven = cars - drivers
##number of cars driving today
cars_driven = drivers
##maximum carpool capacity
carpool_capacity = cars_driven * space_in_a_car
##average number of passengers in one  car
average_passengers_per_car = passengers / cars_driven

#print information
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")