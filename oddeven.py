def greet():
    print("Hello world")


def decideperson():
    age_of_person = int(input("Enter age of Person: "))

    if age_of_person < 18:
        print("Teenager")
    elif age_of_person < 60:
        print("Adult")
    else:
        print("Senior Citizen")


def oddEven():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


def addTwoNumbers():
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    print("Sum =", num1 + num2)


def main():
    greet()
    decideperson()
    oddEven()
    addTwoNumbers()
    
    


if __name__ == "__main__":
    main()
