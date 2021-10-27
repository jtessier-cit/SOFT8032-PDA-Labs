import numpy as np

def q01a():
    """Question 1.
    Write a function that receives two numpy arrays and do the followings:
    1. Find the intersection among two arrays
    2. Remove the intersections from the first array.
    """

    arr1 = np.array([1, 2, 3, 4, 5], int)
    arr2 = np.array([2, 2, 3, 4, 6], int)

    def array_intersect(arr1, arr2):
        # numpy.intersect1d
        # numpy.intersect1d(ar1, ar2, assume_unique=False, return_indices=False)
        intersect = np.intersect1d(arr1, arr2)

    intersect = array_intersect(arr1, arr2)
    print(intersect)
    # subtract the intersection from first array
    # numpy.setdiff1d
    # numpy.setdiff1d(ar1, ar2, assume_unique=False)[source]¶
    print(np.setdiff1d(arr1, arr2))

def q01b():
    """Question 1.
    Write a function that receives two numpy arrays and do the followings:
    1. Find the intersection among two arrays
    2. Remove the intersections from the first array.
    """

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

    # bool_array = np.in1d(arr1, intersect, invert=True)
    bool_array = np.invert(np.in1d(arr1, intersect))
    print(bool_array)

    print(arr1[bool_array])

def q02():
    """Question 2.
    Write a function that receives two numpy arrays. First it should find all the positions where elements
    of two arrays match. Then change the values of those element in the second array to -1. No loop is
    allowed"""
    arr_a = np.array([1, 2, 3, 4, 5], int)
    arr_b = np.array([2, 2, 3, 4, 6], int)

    def q02_funct(arr1, arr2):

        # create a boolean array where elements in first array matche elements in second array
        bool_array = arr1 == arr2
        # print(bool_array)

        # using boolean array for selection, change values to -1
        arr2[bool_array] = -1
        # print(arr2)
        return arr2

    result = q02_funct(arr_a, arr_b)
    print(result)


def q03():
    """Question 3.
    Write a function that takes a numpy array and extract all the elements in a range of [a, b]. a and b are
    read from end user.
    """
    np.random.seed(1)
    a = np.random.randint(1, 100, 10)

    print(a)
    print("Extracting values from range A to B (inclusive).")
    range_low = int(input("Please enter a value on the low end (A):"))
    range_high = int(input("Please enter a value on the upper end (B):"))
    print(f"Extracting values from ({range_low} to {range_high})")

    # boolean array where a >= low range
    array_low = a >=range_low
    print(array_low)

    # boolean array where a <= high range
    array_high = a <=range_high
    print(array_high)

    # combined AND of two boolean arrays
    # gives where values are in both sets
    array_combined = array_low & array_high
    print(array_combined)

    # result is a with True indexes selected
    result = a[array_combined]
    print(result)

    # print sorted result
    print(np.sort(result))
    # print sorted original
    print(np.sort(a))
    # print(in_array >= a)
    # print((in_array <=b))
    # print((in_array >= a) & (in_array <=b))
    # result2 = in_array[(in_array >= a) & (in_array <=b)]
    # print(result2)


def q04():
    print(f"numpy version: {np.__version__}")


def q05():
    """Question 5.
    Write a NumPy program to add a border (filled with 0's) around an existing array.
    """
    np.random.seed(1)
    a = np.random.randint(1, 100, (9,9))
    print(a)

    b = np.pad(a, 1)
    print(b)


def q06():
    """Question 6.
    Write a program that can print all the even days of August 2019.
    """
    import numpy as np

    import random as rnd

    aug = np.arange('2019-08-01', '2019-09-01', dtype='datetime64[D]')
    print(aug)
    evenDays = aug[1::2]

    for i in evenDays:
        print(i)

def q07():
    """Question 7.
    Write a program that asks your date of birth and calculate and print your age as hours. E.g., I
    am 330083 hours old"""


# q01b()
# q02()
q06()