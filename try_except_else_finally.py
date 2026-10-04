while(True):
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
    except:
        print("Invalid input, please enter a valid name and age")
    else:
        print(f"Profile created: {name}, {age} years old")
    finally:
        print("Execution completed")
