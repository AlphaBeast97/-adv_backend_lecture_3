def welcome(function):

    def wrapper():
        print("Welcome to the Student Portal")

        function()

    return wrapper


@welcome
def student():
    print("My name is Ali")
    print("I am enrolled in Backend Development")


student()
