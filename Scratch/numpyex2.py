import time
import numpy as np

def report1():

    data = np.genfromtxt('../dataset/bikeSharing.csv', dtype=float, delimiter=',')

    # Casual Users = 13
    # Registered Users = 14

    # slice data, every row for column 13
    data_casual_users = data[:, 13]

    # slice data, every row for column 13
    data_registered_users = data[:, 14]

    # Print results
    # maximum using np.amax
    print("Maximum Results")
    print(f"\tCasual Users {np.amax(data_casual_users)}")
    print(f"\tRegistered Users {np.amax(data_registered_users)}")
    # minimum using np.amin
    print("Minimum Results")
    print(f"\tCasual Users {np.amin(data_casual_users)}")
    print(f"\tRegistered Users {np.amin(data_registered_users)}")
    # mean using np.mean
    print("Mean Results")
    print(f"\tCasual Users {np.mean(data_casual_users)}")
    print(f"\tRegistered Users {np.mean(data_registered_users)}")


def report2():

    data = np.genfromtxt('../dataset/bikeSharing.csv', dtype=float, delimiter=',')

    # axis = 0 is vertical
    # get an array of the maximums for each column
    resultMaxArr = np.amax(data, axis=0)
    # get an array of the mins for each column
    resultMinArr = np.amin(data, axis=0)
    # get an array of the means for each column
    resultMeanArr = np.mean(data, axis=0)

    # print(resultMaxArr)

    #print results
    # Print results
    # maximum using np.amax
    print("Maximum Results")
    # use index 13 and 14 to get the results for the columns we want
    print(f"\tCasual Users {np.amax(resultMaxArr[13])}")
    print(f"\tRegistered Users {np.amax(resultMaxArr[14])}")
    # minimum using np.amin
    print("Minimum Results")
    print(f"\tCasual Users {np.amin(resultMinArr[13])}")
    print(f"\tRegistered Users {np.amin(resultMinArr[14])}")
    # mean using np.mean
    print("Mean Results")
    print(f"\tCasual Users {np.mean(resultMeanArr[13])}")
    print(f"\tRegistered Users {np.mean(resultMeanArr[14])}")


def report3():
    import numpy as np

    print(np.__version__)

    arr = np.array([10, 15, 20, 25, 30, 35, 40])

    print(arr[1:5:2])
    print(arr[1:4:2])
    # calculate the average wind speed with normal file processing

# time1 = int(round(time.time() * 1000))
# report1()
# time2 = int(round(time.time() * 1000))
# print(time2 - time1)
#
# time1 = int(round(time.time() * 1000))
# report2()
# time2 = int(round(time.time() * 1000))
# print(time2 - time1)

report3()

