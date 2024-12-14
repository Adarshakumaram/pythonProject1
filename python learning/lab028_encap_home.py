class Home:
    def __init__(self):
        self.public_var="Father"
        self.__private_var="child"

    def mom(self):
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("private wife")

h=Home()
h.mom()
print(h.public_var)