from numpy.random import permutation


class Person:
    def __init__(self):
        print("I wil be called")
        self.name=input("entr the name")
        self.age=input("Enter the age")
        self.phone=input("enter the no")
        self.occupation=input("Enter ocuupation")

    def nam_of_the_fun_to_dis(self):
        print(f"name is {self.name}", f"age is {self.age}", f"phone is {self.phone}")

P1 = Person()
P1.nam_of_the_fun_to_dis()