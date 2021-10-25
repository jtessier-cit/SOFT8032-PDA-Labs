import numpy as np
import random as rnd

def q01():
    """Generate a random 1-d numpy array in the range [1-100] and then perform the following: (Note: You are not allowed
    to use any loop to the following tasks).
    1. Extract all the odd numbers
    2. Change the odd numbers to -1
    3. Extract all the even numbers
    4. Increment the even numbers by 1 """

    # initialize an empty numpy array
    arr = np.array([], int)

    # append 100 random ints
    for i in range(100):
        arr = np.append(arr, rnd.randint(1, 100))

    print(arr)

    # another method
    rand_ints = np.random.randint(1, 100, 100)
    print(rand_ints)
    print(type(rand_ints))

    odd_arr = arr[arr % 2 == 1]
    print(odd_arr)

    # assign -1 to all odd values
    arr[arr % 2 == 1] = -1

    print(arr)

    # assign -1 to all odd values
    arr[arr % 2 == 0] += 1
    print(arr)


def q02():
    arr1 = np.array([1, 2, 3, 4, 5], int)
    arr2 = np.array([2, 2, 3, 4, 6], int)

    def array_intersect(arr1, arr2):
        # numpy.intersect1d
        # numpy.intersect1d(ar1, ar2, assume_unique=False, return_indices=False)
        intersect = np.intersect1d(arr1, arr2)
        return intersect

    intersect = array_intersect(arr1, arr2)
    print(intersect)
    # subtract the intersection from first array
    # numpy.setdiff1d
    # numpy.setdiff1d(ar1, ar2, assume_unique=False)[source]¶
    print(np.setdiff1d(arr1, arr2))


def q03a():
    #
    arr_a = np.array([1, 2, 3, 4, 5], int)
    arr_b = np.array([2, 2, 3, 4, 6], int)

    def q03_funct(arr1, arr2):

        # create a boolean array where first array matches second array
        bool_array = arr1 == arr2
        # print(bool_array)

        # using boolean array for selection, change values to -1
        arr2[bool_array] = -1
        # print(arr2)
        return arr2

    result = q03_funct(arr_a, arr_b)
    print(result)


def q03b():
    # a = np.array([1, 3, 5, 6, 9, 10, 14, 15, 56])
    a = np.random.randint(1, 100, 10)
    # a = np.array([2, 4, 15, 25, 42, 67, 72, 73, 75, 99])


    def q04_funct(in_array):
        print(in_array)
        print("Extract values between A and B")
        a = int(input("Please enter the lower bounds (A): "))
        b = int(input("Please enter the upper bounds (B): "))

        result = np.where((in_array >= a) & (in_array <= b))
        print(result)
        # print(in_array >= a)
        # print((in_array <=b))
        # print((in_array >= a) & (in_array <=b))
        # result2 = in_array[(in_array >= a) & (in_array <=b)]
        # print(result2)

    q04_funct(a)


def q04():
    print(np.__version__)


def q05():
    """Write a NumPy program to add a border (filled with 0's) around an existing array.
    """
    # get a 10x10 array
    a = np.random.randint(1, 100, [10,10])
    print(a)

    b = np.pad(a, pad_width=1, constant_values=0)
    print(b)

    c = np.pad(a, pad_width=1, mode='mean')
    print(c)


def q06():
    """Write a program that can find all the unique values in a 2D numpy array.\
    """
    a = np.random.randint(1, 10, [2,5])
    print(a)

    print(np.unique(a))

q06()

