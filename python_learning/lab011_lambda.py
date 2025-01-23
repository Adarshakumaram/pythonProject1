import math
# n=int(input("Enter n "))
# res =  lambda n : n+10
# print(res(n))

res =  lambda n,m : n+m
print(res(12,46))

print("----")

e_o_o = lambda n: "Even" if n%2==0 else "odd"
print(e_o_o(33))

op= lambda : math.pow(int(input("enter num")),2)
print(op())