class Book():
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self) :
        return "name of the book is {}, author is {}, and number of pages are {}".format(self.name,self.author,self.pages)

    def __del__(self):
        print("An object of Book has been deleted")

    def meth(self):
        print("printing here")


book = Book("Alchemist","Paul cohelo","234")
print(book)





