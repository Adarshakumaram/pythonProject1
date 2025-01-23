string='automation'

char_count={}

for char in string:
    char_count[char]=char_count.get(char,0)+1
print(char_count)


#missing keys
dic1={'z':1,'b':2,'c':3}
dic2={'a':4,'b':5}
missing_keys=set(dic1.keys()-dic2.keys())
print(missing_keys)

print(sorted(dic1.keys()))
print(max(dic2.values()))