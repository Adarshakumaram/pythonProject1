browser = input("enter browser name -> ")
match browser:
    case 'chrome':
        print("Starting chrome....!")
    case 'safari':
        print("Starting safari....!")
    case 'edge':
        print("Starting edge....!")
    case _:
        print("Not found")

