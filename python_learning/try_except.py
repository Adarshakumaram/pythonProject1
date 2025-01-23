try:
    a=int(input("a"))
    b=int(input("b"))
    c=a/b
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print(c)
finally:
    print("code ended")


## OS module
import os
print(os.getcwd()) #current working dir
file = os,listdir("/users/")
os.mkdir("TEST")

file_exists= os.path.exists("TEST")
print(file_exists)


import os
try:
  full_path=os.get()
  print(full_path)
  full_path_file=full_path+"/example1"
  print(full_path_file)
  print(os.name)

  file=open(full_path_file)
except Exception as adhu:
  print("File not found")
finally:
  file.close()
  
