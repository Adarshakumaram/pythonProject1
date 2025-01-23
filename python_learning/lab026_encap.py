import os

from dotenv import load_dotenv

class Wlogin:

    def __init__(self,gmail,pwd):
        self.gmail=gmail
        self.pwd =pwd
    def login_confirm(self):
        if self.gmail == 'adhu@gmail.com' and self.pwd == '123':
            print("login succesful")
        else:
            print("login failed")
# log=Wlogin('ads@gmail','234')
# log.login_confirm()
# log=Wlogin('adhu@gmail.com','123')
# log.login_confirm()

load_dotenv()
gmail=os.getenv("gmail")
pwd=os.getenv("pwd")
print(gmail,pwd)
v_obj=Wlogin(gmail,pwd)
v_obj.login_confirm()