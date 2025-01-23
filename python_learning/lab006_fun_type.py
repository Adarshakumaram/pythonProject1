def greet_by_name(name):
    print(f"hello {name}")
greet_by_name("Adhu")
greet_by_name(432)

#defult argu or positional
def greet_by_name(name1="Adhu", name2="k"):
    print("hello", name1, name2)
greet_by_name()
greet_by_name(name1="adarsh")

def sum(a=100,b=200,c=300):
    sum=a+b+c
    return  sum
s=sum()
print(s)
s=sum(2,4,6)
print(s)
