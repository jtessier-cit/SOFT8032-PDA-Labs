def q02():
    # Lab 01 Question 2

    # a) Using script mode write a program that will output the text Hello ‘Python’
    # and in the next line Hello “Python”
    print("Hello 'Python'")
    print('Hello "Python"')

    # b) Create a String variable to store your name in an int variable to store your age.
    # Print this out to screen using the Script mode.
    name = "Some Name"
    age = 30

    # print with comma separated values
    print(name, age)

    # print with concatenation
    print("My name is: " + name)
    print("My age is: " + str(age))

def q03():
    kilometers = int(input("Please enter a distance in Kilometers: "))
    miles = kilometers * 0.6214

    print("The distance is ", miles, " miles.")
    print(type(miles))

def q04():
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter your last name: ")

    moduleGrade1 = int(input("Please enter your grade in module 1: "))
    moduleGrade2 = int(input("Please enter your grade in module 2: "))
    moduleGrade3 = int(input("Please enter your grade in module 3: "))

    average = (moduleGrade1 + moduleGrade2 + moduleGrade3) / 3

    print(firstName, lastName,
          ((moduleGrade1 + moduleGrade2 + moduleGrade3) / 3))

def q05():
    # get info and display BMI
    weightPounds = int(input("Please enter your weight in pounds: "))
    heightInches = int(input("Please enter your height in inches: "))

    # BMI = (weight/ height2 ) * 703
    BMI = (weightPounds / heighInches ** 2) * 703
    print("Your BMI is: ", BMI)

def q06():
    classA = int(input("How many Class A seats were sold? "))
    classB = int(input("How many Class B seats were sold? "))
    classC = int(input("How many Class C seats were sold? "))

    print("The revenue from seats sold is: €", classA * 25 + classB * 20 + classC * 30)

def q07():
    # Write a program that asks the user to enter his/her name and age in year
    # and then calculate the number of months and days and prints the results as follows:

    # Enter your name: Farshad
    # Enter your age: 98
    # Farshad is 1176 months old
    # Farshad is 35770 days old

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(name, "is", age * 12, "months old")
    print(name, "is", age * 365, "years old")

def q08():
    import math
    # Write a program that asks the user to enter radius of a circle and then calculate the area of the circle using the following formula:
    # area= 𝜋𝑟!where 𝜋= 3.14 and r is the radius, then print the value of the area and also prints the type of the variable area.
    # Note: The user is allowed to enter either int or float value.

    radius = float(input("Enter the radius of a circle: "))
    area = math.pi * radius ** 2
    print("The area of the circle is : ", area)
    print("The area variable is of type: ", type(area))


q08()