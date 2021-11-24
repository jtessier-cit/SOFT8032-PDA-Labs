import pandas as pd

# df = pd.read_csv("titanic.csv")


def pClassSurvivorDetails(p_class, df):
    """ I want to print the number
    of males and females that survived and those that
    didn’t from each class."""
    print(f"\nResults for Pclass = {p_class}")
    print("-----------------------------")
    print("The following did not survive:")
    # get values for sex where not survived and pclass = p_class
    # not_survived = df['Survived']==0
    notSurvive = df['Sex'][df['Survived']==0][df['Pclass']==p_class]
    print(notSurvive.value_counts().to_frame())

    print()
    print("The following survived:")
    # get values for sex where survived and pclass = p_class
    survived = df['Sex'][df['Survived']==1][df['Pclass']==p_class]
    print(survived.value_counts().to_frame())


def deaths_by_class(df):
    b_deaths = df['Survived']==0
    all_deaths = df[b_deaths]
    print(f"\nCounts of passengers who died by class")
    print(all_deaths['Pclass'].value_counts().to_frame())

def percent_deaths_by_class(df):
    # boolean set for deaths
    b_deaths = df['Survived']==0
    all_deaths = df[b_deaths]

    # get a series for all passengers by class
    all_passengers = df['Pclass'].value_counts()
    # get a series for deaths by class
    deaths_freq = all_deaths['Pclass'].value_counts()

    # print result
    print(f"\nPercentage of passengers who died by class")
    print(deaths_freq * 100 / all_passengers)

def main():
    df = pd.read_csv("../dataset/titanic.csv")
    for value in [1, 2, 3]:
        pClassSurvivorDetails(value, df)

    deaths_by_class(df)
    percent_deaths_by_class(df)

main()