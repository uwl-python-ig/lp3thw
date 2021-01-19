## ZS: Animal is-a object (yes, sort of confusing) look at the extra credit
## Does "object" below refer to something that is actually defined somewhere?
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a attribute called name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a attribute called name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a attribute called name
        self.name = name

        ## ZS: Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? ZS: hmm what is this strange magic?
        ## BMR this seems to use the specification of the name attribute that is in the superclass
            ## so, this would replace us saying `self.name = name`, we don't need to say that because the name
            ## attribute has already been defined in the superclass, I think
        super(Employee, self).__init__(name)
        ## Person has-a attribute called salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## ZS: rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet (attribute) which is satan
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has a pet (attribute) which is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
