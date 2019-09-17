from usingOneClassInAnotherClass.FirstClass import FirstClass


class SecondFile():
    def __init__(self):
        print("Inside second class")

    def method2(self):
        print("Inside second class method2")

firstClass = FirstClass("firstclass")
firstClass.method1()

secondClass = SecondFile()

if __name__=="__main__":
    secondClass.method2()

