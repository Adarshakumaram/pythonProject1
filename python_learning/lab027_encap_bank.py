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

class Bank:
    def __init__(self,account_number,balance):
        self.balance=balance
        self.__account=account_number

    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance=self.balance+ amount

    def show_account_num(self):
        print(self.__account)
        self.__private_method()


    def __private_method(self):
        print("Private method")

icici=Bank(9889765634,100)
icici.deposit(100)
icici.check_balance()
print(icici.balance)
#print(icici.account-NUMBER) #NOT AVAILABLE
icici.show_account_num()
#icici.__private_method()