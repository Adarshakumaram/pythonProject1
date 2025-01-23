import os
from logging import exception

try:
    full_path = os.getcwd()
    print(full_path)
    full_path_file = full_path+'/example.txt'
    print(full_path_file)

    file= open(full_path_file)

except FileNotFoundError as e:

    print("File not found")
finally:
    print("end of code")