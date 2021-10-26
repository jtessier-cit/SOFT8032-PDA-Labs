
"""
Question 1.
The objective of last week’s exercise was to familiarize yourself with using NumPy in order
to perform basic analysis of a bike sharing dataset. This question focuses specifically on array
based indexing in NumPy.

The following are the details of the various fields from the bike dataset.

0, 1. instant: record index
1, 2. season : season (1:springer, 2:summer, 3:fall, 4:winter)
2, 3. yr : year (0: 2011, 1:2012)
3, 4. mnth : month ( 1 to 12)
4, 5. hr : hour (0 to 23)
5, 6. holiday : whether day is holiday or not (extracted from [Web Link])
6, 7. weekday : day of the week
7, 8. workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
8, 9. + weathersit :
    1: Clear, Few clouds, Partly cloudy, Partly cloudy
    2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
    4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
9, 10. temp : Normalized temperature in Celsius. The values are divided to 41 (max)
10, 11. atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
11, 12. hum: Normalized humidity. The values are divided to 100 (max)
12, 13. windspeed: Normalized wind speed. The values are divided to 67 (max)
13, 14. casual: count of casual users
14, 15. registered: count of registered users
15, 16. cnt: count of total rental bikes including both casual and registered

(i) Read the dataset bikeSharing.csv into a NumPy array.
Write a program that will compare the average number of total users (column index
15) on days that are holidays (1) with the average number of total users on days that
are not holidays (0). Note that you should use array indexing to perform this task.
The above question focuses on both total users, which includes both registered and
casual users. Determine if there is a difference if you only consider casual users
(column index 13).
"""

def q01a():
    # import numpy
    import numpy as np

    # read bikeSharing.csv into a numpy array
    data = np.genfromtxt("../dataset/bikeSharing.csv", delimiter=",")
    print(data.shape)

    # Get boolean array for holidays
    holidays = data[:, 5] == 1


    # Get arrays which hold our casual, registered, total_users
    casual_users = data[:, 13 ]
    registered_users = data[:, 14]
    total_users = data[:, 15]

    total_users_hols = (total_users[holidays])
    total_users_nonhols = (total_users[~holidays])
    # print(f"Count of cells for total users on holidays: {len(total_users_hols)}")
    # print(f"Count of cells for total users on regular days: {len(total_users_nonhols)}")

    print("### Total Users Stats ###")
    print(f"Mean total users on holidays: {np.mean(total_users_hols)}")
    print(f"Mean total users on regular days: {np.mean(total_users_nonhols)}")
    print(f"Mean total users overall: {np.mean(total_users)}")

    casual_users_hols = casual_users[holidays]
    casual_users_nonhols = casual_users[~holidays]
    avg_casual_users_hols = np.mean(casual_users_hols)
    avg_casual_users_nonhols = np.mean(casual_users_nonhols)

    print("\n### Casual Users Stats ###")
    print(f"Mean casual users on holidays: {avg_casual_users_hols}")
    print(f"Mean casual users on regular days: {avg_casual_users_nonhols}")
    print(f"Mean casual users overall: {np.mean(casual_users)}")

    # If we wanted to check the number of lines of holidays matched up
    # print((holidays == True).sum())
    # print((holidays == False).sum())
    # print((holidays == False).sum() + (holidays == True).sum())

    # avg_casual_users = np.mean(casual_users)
    # avg_registered_users = np.mean(registered_users)
    # avg_total_users = np.mean(total_users)
    #
    # print(avg_casual_users)
    # print(avg_registered_users)
    # print(avg_casual_users + avg_registered_users)
    # print(avg_total_users)


def q01_sol():
    import numpy as np
    data = np.genfromtxt("../dataset/bikeSharing.csv", delimiter=',')

    def compareHolidays(data, holiday):
        subset = data[data[:, 5] == holiday]
        print ("Number of entries ", len(subset))
        print ("Mean", np.mean(subset[:, 15]))

    compareHolidays(data, 0)
    compareHolidays(data, 1)


def q01b():
    """ii) You will notice that the following columns in the dataset are normalized:
    • temp : Normalized temperature in Celsius. The values are divided to 41
    (max)
    • atemp: Normalized feeling temperature in Celsius. The values are divided
    to 50 (max)
    • hum: Normalized humidity. The values are divided to 100 (max)
    • windspeed: Normalized wind speed. The values are divided to 67 (max)

    Your objective is to produce a new NumPy array.
    The new NumPy array should be a
    copy of the old with the real-values replacing the normalized values for each of the
    above columns.
    """
    # import numpy
    import numpy as np

    # read bikeSharing.csv into a numpy array
    data = np.genfromtxt("../dataset/bikeSharing.csv", delimiter=",")


    def normalize(arr, column, factor):
        arr[:, column] *= factor
        # return arr

    # create a copy of the array
    new_array = np.copy(data)

    # column 9, temp normalized to 41
    print(new_array[:, 9])
    normalize(new_array, 9, 41)
    print(np.amax(new_array[:, 9]))

    # column 10, atemp normalized to 50
    print(new_array[:, 10])
    normalize(new_array, 10, 50)
    print(np.amax(new_array[:, 10]))

    # column 11, humidity normalized to 100
    print(new_array[:, 11])
    normalize(new_array, 11, 100)
    print(np.amax(new_array[:, 11]))

    # column 12, wind speed normalized to 67
    print(new_array[:, 12])
    normalize(new_array, 12, 67)
    print(np.amax(new_array[:, 12]))


def q01c():
    """(iii) Generally on a given day the number of registered users outnumber the number of
    casual users. Determine the percentage of the days in the dataset where the casual
    users outnumber the registered users (You should be able to do this in 2 or 3 lines
    of code using a relational operator).
    """
    # import numpy
    import numpy as np

    # read bikeSharing.csv into a numpy array
    data = np.genfromtxt("../dataset/bikeSharing.csv", delimiter=",")

    result = data[:, 13] > data[:, 14]
    print(len(result))
    print(len(data))


def q01c_sol():
    # import numpy
    import numpy as np

    data = np.genfromtxt('../dataset/bikeSharing.csv', delimiter=',')

    result = data[:, 13] > data[:, 14]

    print("Percentage of time where causal users > registered", (len(data[result]) * 100.0) / len(data))


# q01a()
# q01_sol()
q01c()
# q01c_sol()