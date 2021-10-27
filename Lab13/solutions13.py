import numpy
import numpy as np


def q01():
    arr = np.random.randint(1, 10, [9,9])
    print(arr)

    # get the length of the array
    array_len = len(arr)
    print(array_len)

    # determine the size of each section
    a = int(len(arr)/3)
    print(a)

    # slice from end of first section to start of 2nd in both dimensions
    res = arr[a:a*2, a:a*2]
    print(res)


def q02():
    """Question 2.
    Write a function that receives a 2D numpy arrays and extract the rows with even index and from those rows extract the second half of the columns.
    """
    arr = np.random.randint(1, 10, [10, 10])
    print(arr)

    even = arr[0::2]
    print(even)

    even = arr[1::2]
    print(even)

    # get half the height of the array
    a = int(len(arr[0])/2)
    print(a)

    print(even[:, a:])


"""
1. instant: record index
2. season : season (1:springer, 2:summer, 3:fall, 4:winter)
3. yr : year (0: 2011, 1:2012)
4. mnth : month ( 1 to 12)
5. hr : hour (0 to 23)
6. holiday : weather day is holiday or not (extracted from [Web Link])
7. weekday : day of the week
8. workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
9. + weathersit :
10. temp : Normalized temperature in Celsius. The values are divided to 41 (max)
11. atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
12. hum: Normalized humidity. The values are divided to 100 (max)
13. windspeed: Normalized wind speed. The values are divided to 67 (max)
14. casual: count of casual users
15. registered: count of registered users
16. cnt: count of total rental bikes including both casual and registered
"""

def q03():
    """Question 3.
    Write a function that reads the bikeSharing file and identify the number of different seasons.
    """
    data = np.genfromtxt('../dataset/bikeSharing.csv', dtype=float, delimiter=',')

    # slice data and get all of column index 1 (seasons), and get unique values
    seasons = np.unique(data[:, 1])
    print(seasons)

    unique_values, occur_count = np.unique(data, return_counts=True)
    print("Unique Values : ", unique_values)
    print("Occurrence Count : ", occur_count)

    # slice data and get all of column index 1 (seasons), and get unique values
    seasons_set = set(data[:,1])
    print(seasons_set)
    print(len(seasons_set))


def q04():
    """Question 4.
    Write a function that reads the bikeSharing file and identify the maximum, minimum and mean temperature of all entries.
    Look at the lecture note to find out the index associated with temperature.
    """
    data = np.genfromtxt('../dataset/bikeSharing.csv', dtype=float, delimiter=',')

    print(np.amin(data[:, 9]*41))
    print(np.amax(data[:, 9]*41))
    print(np.mean(data[:, 9]*41))


q04()