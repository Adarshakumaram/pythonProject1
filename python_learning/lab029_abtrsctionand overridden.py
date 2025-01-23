#Method overloading is not suppuroted in python
print("hello")

#over ridden
class Parent:
    def home(self):
        print("2BHK")
        
class son(Parent):
    def home(self):
        print("3BHK")
    def town(self):
        print("4BHK")
obj=son()
obj.home()
obj.town()



#second

class Oldbrow:
    def start_bro(self):
        print("Starting brow")
        
    def stop_brow(self):
        print("Stop brow")
        
class Chrome(Oldbrow):
    pass

ob=Chrome()
ob.start_bro()
ob.stop_brow()


class Oldbrow:
    def start_bro(self):
        print("Starting brow")
        
    def stop_brow(self):
        print("Stop brow")
        
class Chrome(Oldbrow):
    def start_bro(self):   # new def
        print("Btter brow Starting brow")

ob=Chrome()
ob.start_bro()
ob.stop_brow()

##abstraction

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name=name
        
    @abstractmethod
    def make_noice(self):
        pass
    
class Dog(Animal):
    def make_noice(self):
        print("Bark bark .....")

ob=Dog("Sheera")
ob.make_noice()

from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self,name):
        self.name=name
        
    @abstractmethod
    def loan_pay(self):
        pass
    
class Son(Father):
    def loan_pay(self):
        print("1L paid")

ob=Son("Promod")
ob.loan_pay()

