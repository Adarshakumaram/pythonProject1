try:
    a=12
    b=4
    c = a / b
    print("Result is ", c)
except ZeroDivisionError as e:
    print(e)

except ValueError as a:
    print(a)
finally:
    print("end of the code")