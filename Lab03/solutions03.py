# lab 3

def q01():
    """
    (1) Using conditional statements and logical operators write a python
    code that satisfies the following condition:
    If salary more than 40 and you are older than 25 or if you have worked
    25 years and have kid you can apply for mortgage.
    """

    salary40 = False
    age25 = False
    work25 = True
    kid = True

    if (salary40 and age25) or (work25 and kid):
        print("You can apply")
    else:
        print("Sorry you cannot apply")


def q02():
    """
    (2) Using conditional statements and logical operators write a python
    code that satisfies the following condition:
    If salary more than 40 or you are older than 35 and if you have worked
    10 years or you have kid you can apply for mortgage.
    """

    salary40 = False
    age35 = False
    work10 = True
    kid = True

    if (salary40 or age35) and (work10 or kid):
        print("You can apply")
    else:
        print("Sorry you cannot apply")


q01()
q02()
