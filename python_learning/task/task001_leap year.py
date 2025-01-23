from pickle import PROTO


def leapyear(year):
    if (year%4 == 0 and year%100 !=0) or (year%400 == 0):
        return True
    else:
        return False

year = int(input("Enter year"))

print("yes" if leapyear(year) else "No")