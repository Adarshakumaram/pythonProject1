import time

def timr_dec(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time=time.time()
        print(end_time)
        print("Total time taken by func ->", end_time-start_time)
    return wrapper()



@timr_dec
def test_ui_1():
    print("Add func, time taken buy this func")
    time.sleep(2)
@timr_dec
def test_ui_2():
    print("Add func, time taken buy this func")
    time.sleep(5)
