class Login:


    def __init__(self):
        self.pwd="123"
        self.__pwd="1234" #private instance var
    def change_pwd(self):
        print(self.pwd)
        print(self.__pwd)
obj=Login()
print(obj.pwd)
#print(obj.__pwd)



