#-----------	Object>Animal
## Animal is-a object
class Animal(object):
	def __init__(self, name):
		## ??
		self.name = name

##----------	Object>Animal>Dog
class Dog(Animal):
	pass

#----------		Object>Animal>Cat		
class Cat(Animal):
	pass

#---------		Object>Animal>Person	
class Person(object):

	def __init__(self, name):
		super(Person, self).__init__()
		## Person has a pet of some kind
		self.pet = None

##--------	Object>Animal>Person>
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## ??
class Fish(object):
	pass

## ??
class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

#actual code
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000) #120k

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()