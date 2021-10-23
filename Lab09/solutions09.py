import random


def q01():
    """Question 1.
    Write a function that asks end-user to enter name and studentID for each student
    and store them in a dictionary where the studentID is the key and the name is its value.
    The program should generate appropriate message if end-user tried to provide a key that
    is already existing in the dictionary."""
    students = {}

    entering = True
    while entering:
        student_name = input("Please enter a student name: ")
        student_id = input("Please enter a student id: ")
        if student_id not in students:
            students[student_id] = student_name
        else:
            print(f"Unable to add student {student_id}: already exists")
        print(students)
        user_input = input("Continue y/n ? ") or "Y"
        if user_input.lower().strip()[0] == 'n':
            entering = False


def q02():
    """Question 2.
    Using list to set conversion, write a short function to only find the number of items that are repeated more than once in the list.
    """
    my_list = []
    for i in range(20):
        my_list.append(random.randrange(5))
    my_set = set(my_list)
    print(f"List: {my_list}")
    print(f"Set:  {my_set}")
    print(len(my_list) - len(my_set))


def q03():
    """Question 3.
    Write a Python script to merge two Python dictionaries.
    """
    dict1 = {"1": "one", "2": "two"}
    dict2 = {"2" : "too", "3": "three", "4": "four"}

    dict1.update(dict2)

    print(dict1)



def q04():
    """Question 4.
    Write a Python program to map two lists into a dictionary.
    """
    numeric = [1, 2, 3, 4, 5, 6]
    textual = ["one", "two", "three", "four", "five", "six"]

    new_dict = dict(zip(numeric, textual))
    print(new_dict)

def q05():
    """Question 5.
    Write a function that creates a dictionary using a for loop.
    Keys being the numbers staring from 1 to 10 inclusive and values
    are being some random values in the range [1 - 20] inclusive.
    Then separate the keys from values and add them in two lists.
    """
    my_dict = {}
    for i in range(10):
        my_dict[i+1] = random.randint(1, 20)

    print(my_dict)

    keys = list(my_dict.keys())
    values = list(my_dict.values())
    print(f"Keys: {keys}")
    print(f"Values: {values}")
    print(type(my_dict.keys()))
    print(type(my_dict.values()))

def q06():
    """Question 6.
    Write a Python program to print all unique values in a dictionary.
    """
    my_dict = {}
    for i in range(10):
        my_dict[i+1] = random.randrange(5)

    print(my_dict)

    unique_values = set(my_dict.values())
    print(f"Values: {unique_values}")


def q07():
    """Question 7.
    Write a function that takes two sets as input, then it should returns only those values that were not common among both sets.
    """
    def setSymDif(set1, set2):
        return set1.symmetric_difference(set2)

    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}

    print(setSymDif(set_a, set_b))

def q08():
    """Question 8.
    Write a program that goes through a list and extract only integer values and add them in a new list.
    """
    my_list = [1, "Not", 2, "An" , "Integer"]
    integers = []
    for i in my_list:
        if type(i) == int:
            integers.append(i)

    print(integers)

def q09():
    """Question 9.
    Repeat the previous program this time only extract unique numbers (integer).
    """
    my_list = [1, "Not", 2, "An" , "Integer", 3, 2]
    integers = set()
    for i in my_list:
        if type(i) == int:
            integers.add(i)

    print(integers)


def q10():
    """Question 10.
    Use an appropriate data structure and ask end-user to repeatedly enter some names. You need to ensure that the items in that data structure can not be altered or updated later on.
    """
    my_list = []
    for i in range(3):
        item = input("Please input a name: ")
        my_list.append(item)

    my_tuple = tuple(my_list)
    print(type(my_tuple))
    print(my_tuple)




q10()