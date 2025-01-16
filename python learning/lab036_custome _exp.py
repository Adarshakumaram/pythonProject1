class lowBalanceExc(Exception):
    def __init__(self,msg):
        self.msg=msg
        super().__init__(msg)

balance =100
withdraw=int(input("enter value"))
if withdraw > balance:
    raise lowBalanceExc("balance is no")
else:
    print("balance is ",(balance-withdraw))