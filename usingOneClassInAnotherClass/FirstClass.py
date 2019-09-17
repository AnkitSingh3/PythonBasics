class FirstClass:
    def __init__(self,var1):
        print("Inside FirstClass")
        self.var1 = var1

    def method1(self):
        print("value of variable is: " + self.var1)

if __name__=="__main__":
    print("this class has been run directly")
else:
    print("doesnt")