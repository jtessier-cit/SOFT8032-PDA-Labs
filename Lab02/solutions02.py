# Lab 2

def q01():
    # Write a program that determine the tax rate based on two factors:
    # salary and having kids or not:
    # If salary is in range of [30, 50] and the employee does not have kid tax is 40,
    # if the salary is still in range of [30, 50] but the employee has kid tax is 35.
    # If salary in range of [50, 70] and the employee does not have kid tax is 50
    # if the salary is still in range of [50, 70] but the employee has kid then tax is 45.
    # If salary is less then 30 tax is 0
    # no matter if the employee has kid or not
    # and if the salary is more then 70 the tax is 55 no matter if the employee has kid or not.

    salary = 30
    hasKid = True
    tax = 0

    if salary > 70:     # > 70
        tax = 55
    elif salary >= 50:  # 50-70
        if hasKid:
            tax = 45
        else:
            tax = 50
    elif salary >= 30:  # 30-50
        if hasKid:
            tax = 35
        else:
            tax = 40
    else:               # < 30
        tax = 0

    print("Tax rate on salary", salary, "when hasKid", hasKid, "is", tax)


q01()