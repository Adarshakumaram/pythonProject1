a=10

class Person:
    b=11 # instance - belong to class

    def print_per(self):
        c=20  #local variable
        a = "hello" #local
        print(c)
        print(self.b)
        print(a)



obj_reff = Person()
obj_reff.print_per()