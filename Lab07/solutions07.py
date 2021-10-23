import math
import random


def powerV1():
    """Question 1i
    Write a function called powerV1. When you call this function (from your main function)
    it should ask the user for a base number and a power number.
    It should then print out the result of raising the base number to the power of the second number.

    Sample output below:
    Please enter base number: 3
    Please enter power number: 2
    The value 3 raised to the power of 2 is : 9
    """

    base_num = int(input("Please enter base number: "))
    power_num = int(input("Please enter power number: "))
    result = base_num ** power_num
    print(f"The value {base_num} raised to the power of {power_num} is: {result}")


def powerV2():
    """Question 1ii
    Given the following equation: 𝐴 = 𝐵^C
    Write a function called powerV2. When you call this function (from your main function)
    it should ask the user for the power number (C) and the result (A).
    It should then print out the base number. (Hint you need to use math module).
    """

    base_num = int(input("Please enter power number: "))
    result_num = int(input("Please enter result number: "))
    log_num = math.log(result_num, base_num)
    print(f"The logarithm of {result_num} with base {base_num} is: {log_num}")


def generateRandomNumber():
    limit = 100
    return random.randint(0, limit)


def askUser():
    guess = -1
    while guess < 0 or guess > 100:
        guess = int(input("Please enter your guess: "))

    return guess


def checkGuess(num, guess):
    if (num == guess):
        return True
    elif (num > guess):
        print("Too low")
        return False
    elif (num < guess):
        print("Too high")
        return False
    else:
        print("Bad state")
        return False


def recur_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recur_factorial(n - 1)


def q02():
    random_num = generateRandomNumber()
    print("Program has generated a random number.")
    guess = askUser()
    num_guesses = 1
    while not checkGuess(random_num, guess):
        num_guesses += 1
        guess = askUser()

    print(f"Correct. You made a total of {num_guesses} guesses to find {random_num}")


def q03():
    n = int(input("Please enter the factorial number you want to see: "))
    for i in range(n + 1):
        print(f"{i}: {recur_factorial(i)}")


import mymod


def q04():
    numbers = []
    for i in range(5):
        numbers.append(random.randint(0, 10))
    print(numbers)
    print(f"average of numbers: {mymod.average5(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])}")
    print(f"max of numbers: {mymod.max5(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])}")
    print(f"min of numbers: {mymod.min5(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])}")
    print(f"numbers sorted: {mymod.sort5(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])}")
    print(f"sum of numbers: {mymod.sum5(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])}")

def q05():
    x = int(input("Enter X: "))
    y = int(input("Enter Y: "))
    point = [x, y]
    origin = [0, 0]
    distance = math.dist(origin, point)
    print(f"Euclidean distance: {distance}")


def main():
    # powerV1()
    # powerV2()
    # print(generateRandomNumber())
    # print(askUser())
    # print(checkGuess(3,4))
    # q02()
    # q03()
    # q04()
    q05()

main()
