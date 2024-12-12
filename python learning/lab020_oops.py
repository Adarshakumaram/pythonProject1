class Dog:
    name=None
    breed=None
    height=None

    def __init__(self,name,breed):
        print("I will call")
        self.name=name
        self.breed=breed

    def sleep(self):
        print("who is sleeping  "+self.name)

    def bark(self):
        print("Bark")
    def talk(self):
        pass

#OBJ  ref
chow_ref= Dog("chow","BB")
print(chow_ref.name)
print(chow_ref.sleep())

mhow_ref= Dog("mow","QQ")
print(mhow_ref.name)
print(mhow_ref.sleep())
print(id(chow_ref))