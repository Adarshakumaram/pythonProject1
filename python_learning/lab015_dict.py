my_dict={
    'name':'adhu',
    'age' : 26,
    'Role' : 'SDET',
    'expi' : 3
}

print(my_dict)
print(my_dict['name'])
my_dict['Role'] = 'Automation'
print(my_dict)

del my_dict['age']
print(my_dict)

for key,value in  my_dict.items():
    print(key,value)