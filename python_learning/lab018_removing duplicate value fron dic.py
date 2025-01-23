dic1={'z':1,'b':2,'c':3}

result={}
unique_value=set()

for key,value in dic1.items():
    if value not in unique_value:
        result[key]=value
        unique_value.add(value)
print(result)