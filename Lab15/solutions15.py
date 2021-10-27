
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
    casual_users = data[:, 13]
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

    # boolean result
    result = data[:, 13] > data[:, 14]
    print(result)
    days = (len(data[result]))
    total_days = (len(data))

    percent = days * 100 / total_days
    # print(percent)
    print(f"Percentage of days where casual users is greater than registered users: {percent}%.")



def q01c_sol():
    # import numpy
    import numpy as np

    data = np.genfromtxt('../dataset/bikeSharing.csv', delimiter=',')

    result = data[:, 13] > data[:, 14]

    print("Percentage of time where causal users > registered", (len(data[result]) * 100.0) / len(data))


def q01d():
    """In this question you should provide a new implementation of one of last week’s questions using array indexing. The
    objective of this task is to investigate the impact of weather conditions on the popularity of the bike scheme. For
    each of the 4 possible weather conditions calculate the average number of rental bikes.

    Average number of bikes is 189.463087635
    Average bikes for condition Clear is 204.869271883
    Average bikes for condition Mist and Cloudy is 175.165492958
    Average bikes for condition Light Rain is 111.579281184
    Average bikes for condition Heavy Rain is 74.3333333333"""

    # import numpy
    import numpy as np

    # read bikeSharing.csv into a numpy array
    data = np.genfromtxt("../dataset/bikeSharing.csv", delimiter=",")
    print(data.shape)

    # get mean of column 15 which is total of bikes/day
    bikes = data[:, 15]
    mean_bikes = np.mean(bikes)

    #    8, 9. + weathersit:
    # column 8, weather situation
    # slices for each condition
    # 1: Clear, Few clouds, Partly cloudy, Partly cloudy
    # 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    # 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
    # 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
    bool_clear = data[:, 8] == 1
    bool_mist = data[:, 8] == 2
    bool_light = data[:, 8] == 3
    bool_heavy = data[:, 8] == 4

    print(bool_clear)
    print(bool_mist)
    print(bool_light)
    print(bool_heavy)

    mean_clear = np.mean(bikes[bool_clear])
    mean_mist = np.mean(bikes[bool_mist])
    mean_light = np.mean(bikes[bool_light])
    mean_heavy = np.mean(bikes[bool_heavy])
    print(f"Average number of bikes is: {mean_bikes}")
    print(f"Average number of bikes for condition clear: {mean_clear}")
    print(f"Average number of bikes for condition mist: {mean_mist}")
    print(f"Average number of bikes for condition light: {mean_light}")
    print(f"Average number of bikes for condition heavy: {mean_heavy}")


def q01e():
    """
    The objective of this question is to look at the relationship between temperature and the number of casual users.
    Your code should work out the average number of casual users for the following temperature ranges:
    1, 5
    6, 10
    11, 15
    16, 20
    21, 25
    26, 30
    31, 35
    36, 40

    Please note the temperature range specified in the file have been normalised by dividing by 41
    The following is the sample output:
    For temp in range 1 to 5 the mean number of casual users was 49.2954545455
    For temp in range 6 to 10 the mean number of casual users was 73.6670630202
    For temp in range 11 to 15 the mean number of casual users was 130.681770652
    For temp in range 16 to 20 the mean number of casual users was 169.066772655
    For temp in range 21 to 25 the mean number of casual users was 211.700074516
    For temp in range 26 to 30 the mean number of casual users was 242.172678691
    For temp in range 31 to 35 the mean number of casual users was 337.473005641
    For temp in range 36 to 40 the mean number of casual users was 314.991111111
    """
    # import numpy
    import numpy as np

    # read bikeSharing.csv into a numpy array
    data = np.genfromtxt("../dataset/bikeSharing.csv", delimiter=",")
    # print(data.shape)

    # get mean of column 13 which is casual users
    casual_users = data[:, 13]

    # column 9, temp normalized to 41
    temp = data[:, 9] * 41
    print(temp)
    print(len(temp))
    print(np.amax(temp))

    def mean_users(low, high):
        arr_low = temp >= low
        # print(arr_low)
        arr_high = temp <= high
        # print(arr_high)
        arr_combination = (arr_low & arr_high)
        # print(arr_combination)
        subset = casual_users[arr_combination]
        # print((subset))
        print(f"Temp range {low} to {high} mean users: {np.mean(subset)}")

    mean_users(1, 5)
    for t in range (1, 40, 5):
        mean_users(t, t+4)


def q01e_sol():
    # import numpy
    import numpy as np

    # read bikeSharing.csv into a numpy array
    data = np.genfromtxt("../dataset/bikeSharing.csv", delimiter=",")



    def analyseTemp(data, minValue, maxValue):
        # the temperature values stored in the array are multiplied by 41
        higherTempCondition = (data[:, 9] * 41) >= minValue
        lowerTempCondition = (data[:, 9] * 41) <= maxValue
        subset = data[higherTempCondition & lowerTempCondition]
        meanValue = np.mean(subset[:, 13])
        print("For temp in range ", minValue, "to", maxValue, "the mean number of casual users was ", meanValue)


    for temp in range(1, 40, 5):
        analyseTemp(data, temp, temp + 4)



q01a()
# q01_sol()
# q01e()
# q01c_sol()