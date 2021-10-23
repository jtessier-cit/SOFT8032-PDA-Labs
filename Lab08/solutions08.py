def q01a():
    try:
        num1 = int(input('Enter the first number '))
        num2 = int(input('Enter the second number '))
    except:
        print("You must enter an integer value only.")
    else:
        average = (num1 + num2) / 2
        print(average)

def q01b():
    input_valid = False
    while not input_valid:
        try:
            num1 = int(input('Enter the first number '))
            num2 = int(input('Enter the second number '))
        except ValueError:
            print("You must enter an integer value only.")
        else:
            input_valid = True
            average = (num1 + num2) / 2
            print(average)


def q03():
    try:
        fileContent = open("tes.txt", "r")
        line = fileContent.readline()
        print(line)
        number = int(line)
        print(number)
        fileContent.close()
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print(f"Could not convert {line} to int.")
    else:
        print("No errors occurred")
    finally:
        print("In finally")


def q03():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    assert num2 != 0, f"num2 must be non-zero. Entered {num2}"

    print(num1/num2)
q03()