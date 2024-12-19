
class o():
    @staticmethod
    def sum(a,b):
        return a+b
        
    def sub(a,b):
        return a-b
ob=o()
res=o.sub(28,4)
print(res)

print("-----")

print(o.sum(3,5)) #static call
