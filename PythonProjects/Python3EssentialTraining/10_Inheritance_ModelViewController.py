
#-------------------------------------------------------------------
# Lesson 10: Greater reusability with inheritance and polymorphism
#-------------------------------------------------------------------

# Each class (Duck, Person, Dog) inherites "AnimalActions" class
# Class AnimalActions has 4 methods
# Other classes have dictionaries with different strings

# Each method of AnimalAction class becomes avaliable for each other class

# -- VIEW --

class AnimalActions:
    def quack(self): return self._doAction('quack')
    def feathers(self): return self._doAction('feathers')
    def bark(self): return self._doAction('bark')
    def fur(self): return self._doAction('fur')

    def _doAction(self, action):
        if action in self.strings:
            return self.strings[action]
        else:
            return 'The {} has no {}'.format(self.animalName(), action)

    def animalName(self):
        return self.__class__.__name__.lower()


# -- MODEL

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaak!",
        feathers = "The duck has grey and white feathers.",
    )

class Person(AnimalActions):
    strings = dict(
        quack = "The person imitates a duck.",
        feathers = "The person takes a feather from the ground and shows it.",
        bark = "The person says woof!",
        fur = "The person puts on a fur coat."
    )

class Dog(AnimalActions):
    strings = dict(
        bark = "Arf!",
        fur = "The dog has white fur with black spots."
    )


# -- CONTROLLER --

def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())

def main():
    donad = Duck()
    john = Person()
    fido = Dog()

    print("- In the forest:")
    for o in (donad, john, fido):
        in_the_doghouse(o)

    print("- In the doghouse:")
    for o in (donad, john, fido):
        in_the_doghouse(o)

if __name__ == "__main__":
    main()
