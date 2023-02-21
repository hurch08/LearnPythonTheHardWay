## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## is-a relationship
class Dog(Animal):

    def __init__(self, name):
        ## has-a relationship
        self.name = name

## is-a relationship
class Cat(Animal):

    def __init__(self, name):
        ## has-a relationship
        self.name = name

## is-a relationship
class Person(object):

    def __init__(self, name):
        ## has-a relationship
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

## is-a relationship
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## has-a relationship
        self.salary = salary

## is-a relationship
class Fish(object):
    pass

## is-a relationship
class Salmon(Fish):
    pass

## is-a relationship
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## is-a relationship
satan = Cat("Satan")

## is-a relationship
mary = Person("Mary")

## has-a relationship
mary.pet = satan

## has-a relationship
frank = Employee("Frank", 120000)

## has-a relationship
flipper = Fish()

## has-a relationship
crouse = Salmon()

## has-a relationship
harry = Halibut()
## 
