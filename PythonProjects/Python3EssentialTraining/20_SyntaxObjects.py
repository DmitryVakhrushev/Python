
# Lesson 20 -- Creating and using objects

class Egg:
    def __init__(self, kind = "Fried"):
        self._kind = kind

    def whatKind(self):
        return self._kind


def main():
    fried = Egg() # initiate the object fo the class "Egg"
    scrambled = Egg("Scrambled")

    print (fried.whatKind())
    print(scrambled.whatKind())

if __name__ == "__main__": main()


