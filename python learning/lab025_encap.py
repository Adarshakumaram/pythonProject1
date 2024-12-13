class Car:
    def __init__(self,name,make,model):
        self.name=name
        self.make=make
        self.model=model

    def start_engine(self):
        print("starting engine "+ self.name)
        print("starting engine "+ self.make)
        print("starting engine "+ self.model)
lam=Car("lambo","V6","2023")
lam.start_engine()
mg=Car("Hector","Turbo","2024")
mg.start_engine()