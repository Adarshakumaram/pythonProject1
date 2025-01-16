file_name='adhu.txt'
content="this is adhu's file asd"

with open(file_name,'w') as file:
    file.write(content)
    file.close()

with open(file_name,'r') as file1:
    content1=file1.read()
    print(content1)
