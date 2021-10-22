def q01():
    """(Basic if/elif statements)
    The area of a rectangle is the length multiplied by width. Write a program that asks for the
    length and width of two rectangles. The program should tell the user which rectangle has the
    greater area or if the areas are the same.
    """
    width1 = int(input("Enter width of first rectangle: "))
    height1 = int(input("Enter height of first rectangle: "))

    width2 = int(input("Enter width of second rectangle: "))
    height2 = int(input("Enter height of second rectangle: "))

    area1 = width1 * height1
    area2 = width2 * height2

    if area1 > area2:
        print(f"Rectangle 1 is greater with an area of {area1} units squared.")
    elif area2 > area1:
        print(f"Rectangle 2 is greater with an area of {area2} units squared.")
    else:
        print(f"Rectangle 1 ({area1}) and Rectangle 2 ({area2}) are equal.")

def q02a():
    """A development company will only employ an individual if they have a minimum of 4 years
    of commercial software development experience, a Microsoft certification and a first class
    honours undergraduate computing degree.

    (i) Write a program that will use nested if statements to determine if a user is
    sufficiently qualified to be employed. The first if statement should check if the
    user has 4 years of commercial software development experience, the second
    nested if statement should check if they have a Microsoft certification and the
    final nested if statement should check if the user has a first class honours
    undergraduate computing degree.

    If the user does not satisfy one of the conditions the program should inform the
    user that they are not eligible and should also inform the user of the requirement
    they have failed. The program should then exit.

    How many years of commercial software development experience do you have: 5
    Do you hold a Microsoft certification y/n: n
    You are not eligible. You need to hold a Microsoft certification.
    """
    years_experience = int(input("How many years of commercial software development experience do you have: "))
    if years_experience < 4:
        print("You are not eligible. You must have 4 years of experience.")
    else:
        certification = input("Do you hold a Microsoft certification? (y/n) ")
        if certification.lower() != "y":
            print("You are not eligible. You need to hold a Microsoft certification.")
        else:
            honours = input("Do you have a first class honours undergraduate computing degree? (y/n) ")
            if honours.lower() != "y":
                print("You are not eligible. You must have a first class honours undergraduate computing degree.")
            else:
                print("Congratulations, you are eligible")


def q02b():

    """ Rewrite the above program so you only use only a single if statement to check that
    the user satisfies the above conditions to be employed (you will need to use an
    and logical operator). Please note this version of the program will ask the user to
    enter all relevant information first and will then inform the user if they are eligible
    or not. Note it doesn’t need to inform the user of the specific reasons as to why
    they were not accepted.

    How many years of commercial software development experience do you have: 3
    Do you hold a Microsoft certification y/n: y
    Do you have a first class honours primary degree y/n: y
    You are not eligible for this position. """

    years_experience = int(input("How many years of commercial software development experience do you have: "))
    certification = input("Do you hold a Microsoft certification? (y/n) ")
    honours = input("Do you have a first class honours undergraduate computing degree? (y/n) ")
    if years_experience < 4 or certification.lower() != "y" or honours.lower() != "y":
        print("You are not eligible.")
    else:
        print("Congratulations, you are eligible")

def q03():
    """(if elif Statements)
    A software company sells a package that retails for €99. Quantity discounts are given
    according to the following table.

    Quantity Discount
    1 – 9 0%
    10 – 19 20%
    20 – 49 30%
    50 – 99 40%
    100 or more 50%

    Write a program that will ask the user to enter the number of packages purchased. The
    program should display the amount of the discount (if any) and the total amount of the
    purchase after the discount. Please note that if a user indicates a negative quantity then they
    should be told that the quantity value should be greater than zero.

    Please use if elif statements to solve this problem and note that your solution to this problem
    should make use of the and logical operator where possible.
    """

    discount = """
    Quantity Discount
    1 – 9 0%
    10 – 19 20%
    20 – 49 30%
    50 – 99 40%
    100 or more 50%"""

    #print("How many packages would you like to purchase?")
    #print(discount)

    qty = int(input("Enter quantity: "))
    if qty > 99:
        print(f"For {qty} packages, discount is 50%")
    elif qty > 49:
        print(f"For {qty} packages, discount is 40%")
    elif qty > 19:
        print(f"For {qty} packages, discount is 30%")
    elif qty > 9:
        print(f"For {qty} packages, discount is 20%")
    elif qty > 0:
        print(f"For {qty} packages, discount is 0%")
    else:
        print("Please enter a number > 0")

def q04a():
    """
    (for loops and functions)
    (i)
    You should write a function that will print out the ‘times’ table for a number up to a specific
    limit. The function should take in two parameters. The first value, num, is the number that we
    will multiply by 0, 1, 2, 3, etc. The second number, limit, is the number at which we will stop
    multiplying
    So if the user enters 3 as the value of num and 5 as the value of limit then the program will
    output the 3 times table from 0 to 5 as shown below.
    • 3*0
    • 3*1
    • 3*2
    • 3*3
    • 3*4
    • 3*5
    The following is a sample output:
    Please enter time tables for printing: 6
    Please enter upper limit for multiplication: 4
    6*0 = 0
    6*1 = 6
    6*2 = 12
    6*3 = 18
    6*4 = 24
    """
    multiplicand = int(input("Please enter the multiplicand: "))
    limit = int(input("Please enter the multiplier: "))

    for multiplier in range (limit+1):
        print(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")

def printNumTriangle():
    triangleSize = int(input("Please enter an integer for triangle size: "))

    for i in range(1,triangleSize+1):
        triangleLine = str(i) * i
        # print(f"{i}" * i)
        print(triangleLine)



def q04b():
    """
    Implement a function called printNumTriangle. The function should ask the user to enter a
    single integer. It should then print a triangle of that size specified by the integer so that each
    row in the triangle is made up of the integer displayed.
    The following is a sample output
    Please enter an integer for triangle size: 5
    1
    22
    333
    4444
    55555
    """
    printNumTriangle()


def q05():
    """
    Write a program that asks the user to enter the rainfall for the first X months of the year into a
    list, where X is an int value between 1 and 12. (Obtaining the rainfall input from the user
    should be done using a loop).

    The program should calculate and display:
    • The average monthly rainfall
    • The highest rainfall value received
    • The lowest rainfall value received

    The following is a sample output of this program.

    How many months of data do you wish to enter: 6
    Please enter rainfall for month1 83.6
    Please enter rainfall for month2 46.6
    Please enter rainfall for month3 97.1
    Please enter rainfall for month4 46.4
    Please enter rainfall for month5 61.4
    Please enter rainfall for month6 164.5
    Highest rainfall value: 164.5
    Lowest rainfall value: 46.4
    Average is 83.2666666667
    """
    num_months = int(input("How many months of data do you wish to enter: "))

    rainfall_list = []
    for month in range(1, num_months + 1):
        rainfall_amt = float(input(f"Please enter rainfall for month {month}: "))
        rainfall_list.append(rainfall_amt)

    max_rainfall = max(rainfall_list)
    min_rainfall = min(rainfall_list)
    avg_rainfall = sum(rainfall_list) / len(rainfall_list)

    print(f"Highest rainfall value: {max_rainfall}")
    print(f"Lowest rainfall value: {min_rainfall}")
    print(f"Average is: {avg_rainfall}")
    # print(rainfall_list)

def q06():
    """
    The Fibonacci numbers are the numbers in the following integer sequence:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
    By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each
    subsequent number is the sum of the previous two.
    Create a program that creates a list and will populate it with the first 40 Fibonacci numbers
    (this can be done with just three lines of code).
    The program should then ask the user to enter an integer value between 1 and 40 to indicate
    which number in the Fibonacci series they would like to see and the application should
    display that number. For example, if the user enters 13, the 13th number is 144.
    """

    fibs = []
    for i in range(40):
        if i == 0:
            fibs.append(0)
            # print(i, fibs)
        elif i == 1:
            fibs.append(1)
            # print(i, fibs)
        else:
            fib_n = fibs[i-1] + fibs[i-2]
            fibs.append(fib_n)
            # print(i, fibs)


    fib_number = int(input("Which fibonacci number would you like to see (1-40)? "))
    print(fibs[fib_number - 1])

def q07():
    """
    Write a program that will act as a basic calculator for the user. The program should first ask
    the user for two separate numerical values. It should then give the user an option to perform
    one of four operations: addition, subtraction, division or multiplication. Therefore, if the user
    selects multiplication then your program should print out the product of the two values. The
    following is sample output from this program.

    Please enter a numerical value: 12
    Please enter a numerical value: 10
    Would you like to perform:
    1: Addition
    2. Subtraction
    3. Multiplication
    4 Division
    > 3
    Multiplication of 12 and 10 is 120
    """

    num1 = int(input("Please enter a numerical value: "))
    num2 = int(input("Please enter another numerical value: "))

    print("Would you like to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = -1
    while choice not in range(1,5):
        choice = int(input("> "))

    if choice == 1:
        print(f"Addition of {num1} and {num2} is {num1 + num2}")
    elif choice == 2:
        print(f"Subtraction of {num1} and {num2} is {num1 - num2}")
    elif choice == 3:
        print(f"Multiplication of {num1} and {num2} is {num1 * num2}")
    elif choice == 4:
        print(f"Division of {num1} and {num2} is {num1 / num2}")


q07()