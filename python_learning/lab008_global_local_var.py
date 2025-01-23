pub_glob="PT"
def home():
    private_loc="private"
    print(private_loc)
    print(pub_glob)

home()

def outer_fun():
    var1=30 #globla for below def
    def inner_fun():
        print(var1)
    inner_fun()
    def inner_fun1():
        print(var1)
    inner_fun1()

outer_fun()