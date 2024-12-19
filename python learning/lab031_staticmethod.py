
class o():
    @staticmethod
    def sum(a,b):
        return a+b
        
    def sub(a,b):
        return a-b
ob=o()
res=o.sub(28,4)
print(res)

print("-----")

print(o.sum(3,5)) #static call



###doubt

from abc import ABC, abstractmethod

class Bankaccount:
    def __init__(account_n,ammount):
        self.acc=account
        self.amt=ammount
    
class ICICI(Bankaccount):
    def withdrw(self):
        print("yes")
        
    @abstractmethod
    def loan(self):
        pass
    
    @staticmethod
    def static_meth(self):
        print("calling")
        
print(a.static_meth())
