import os
from logging import exception


class XYZ:
    def f1(self):
        try:
            a=int(input("enter value"))
        except Exception as a:
            print("Enter int only")
        else:
            print(a)
        finally:
            print("code ended")
obj = XYZ()
obj.f1()