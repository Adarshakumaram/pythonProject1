

def add_before_and_after_code(func):
    def before():
        print("1. Before running UI tc")
        print("2. Start the browser")
        func()
        print("3 After running the UI tc")
        print("4. close browser")
    return before()

@add_before_and_after_code
def test_ui():
    print(">> i will test the UI")

@add_before_and_after_code
def done():
    print("Done")




