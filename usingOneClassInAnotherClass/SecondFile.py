from usingOneClassInAnotherClass.FirstClass import FirstClass


class SecondFile():
    def __init__(self):
        print("Inside second class")

firstClass = FirstClass("firstclass")
firstClass.method1()

