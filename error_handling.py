try:
    number = int(input("Enter a number: "))
    result = 500 / number
    print(f"Result: {result}")

except ValueError:
    print("That was not a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")
