from multiprocessing.managers import Value


def value(*args):
    for i in args:
        print(i)
value("ADHU")
value("DS","DH","DRT")