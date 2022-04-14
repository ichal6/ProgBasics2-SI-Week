import sys


while 1:
    first = input("Enter a number (or a letter to exit): ")
    if not(first.isdigit()):
        sys.exit()
    command = input("Enter an operation: ")
    second = input("Enter another number: ")
    if command == '*':
        result = int(first) * int(second)
    elif command == '+':
        result = int(first) + int(second)
    elif command == '-':
        result = int(first) - int(second)
    elif command == '/':
        if int(second) == 0:
            sys.exit()
        else:
            result = (int(first) / int(second))
    print("Result: " + str(result) + "\n\n\n\n")
