student_info = dict(name='adarsh',age='26',Address='KA')
print(student_info)

key=['name','role','age']
value=['Raj','Sdet',3]
dic=dict(zip(key,value))
print(dic)

dic1 = {'a':1,'b':2}
dic2 = {'c':3,'d':4}
merge_dic = dic1 | dic2
print(merge_dic)
print(merge_dic['a'])