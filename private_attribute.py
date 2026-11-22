class myClass:
    __privateVar = 27;
    def __privMeth(self):
        print("I am inside class myClass")
    def hello(self):
        print("private variable is: ", self.__privateVar)

foo = myClass()
foo.hello()
foo.__privateVar
