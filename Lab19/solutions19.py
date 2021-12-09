import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def q01():
    """Using bar chart, visualize the distribution of two groups of passengers:
    1) those who are older than 30
    2) those who are younger than 30"""
    df = pd.read_csv("../dataset/titanic.csv",encoding = "ISO-8859-1")

    trim_df = df[['Age']]

    filt_lt_30 = trim_df[trim_df['Age']< 30]
    filt_gt_30 = trim_df[trim_df['Age']> 30]

    indexes = ['Younger than 30', 'Older than 30']
    population = [len(filt_lt_30), len(filt_gt_30)]
    plt.bar(indexes, population)
    plt.show()

def q02():
    """Repeat the previous question and this time separate male and female. See figure below:"""

    df = pd.read_csv("../dataset/titanic.csv",encoding = "ISO-8859-1")

    df = df[['Age', 'Sex']]

    bool_lt_30 = df['Age'] < 30
    bool_gt_30 = df['Age'] > 30

    bool_male = df['Sex'] == 'male'
    bool_female = df['Sex'] == 'female'

    m_lt_30 = df[bool_lt_30 & bool_male]
    m_gt_30 = df[bool_gt_30 & bool_male]

    f_lt_30 = df[bool_lt_30 & bool_female]
    f_gt_30 = df[bool_gt_30 & bool_female]

    pop_male = [len(m_lt_30), len(m_gt_30)]
    pop_female = [len(f_lt_30), len(f_gt_30)]

    labels = ['Younger than 30', 'Older than 30']
    indexes = np.arange(1,3)
    bar_width = 0.3
    plt.bar(indexes, pop_male, bar_width)
    plt.bar(indexes + bar_width, pop_female, bar_width)
    plt.xticks(indexes + bar_width/2, labels)
    plt.legend(['Male','Female'])
    plt.show()


def q03():
    """Use scatter plot and visualize the data where the x coordinate of each point is the age of the
    passenger and the y coordinate is their fare. What age (approximately) had the most expensive
    ticket?"""
    df = pd.read_csv("../dataset/titanic.csv",encoding = "ISO-8859-1")

    df = df[['Age', 'Fare']].dropna()
    print(df)

    area = np.pi * (np.random.rand()*1)
    plt.scatter(df['Age'],df['Fare'], s=area,  color='r')
    plt.show()


def q04():
    """Use Histogram and visualize the distribution of the passengers’ age. Use the comment and interpret the
    visual result."""
    df = pd.read_csv("../dataset/titanic.csv",encoding = "ISO-8859-1")

    df = df[['Age']].dropna()

    plt.hist(df, bins=40)
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()



def q05i():
    """Use an appropriate visualization technique and analyse the outliers in
    1) Passengers ages
    2) Passengers
    Ticket Fare."""
    df = pd.read_csv("../dataset/titanic.csv",encoding = "ISO-8859-1")

    fares = df['Fare'].dropna()
    plt.boxplot(fares)
    plt.xlabel("Fare")
    plt.show()


def q05ii():
    """Use an appropriate visualization technique and analyse the outliers in
    1) Passengers ages
    2) Passengers
    Ticket Fare."""
    df = pd.read_csv("../dataset/titanic.csv",encoding = "ISO-8859-1")

    fares = df['Age'].dropna()
    plt.boxplot(fares)
    plt.xlabel("Age")
    plt.show()

def q06():
    """Use pie-chart and visualize the four different age clusters:
    1) age<25
    2) 25<= age <50
    3) 50<=age <75
    4) age>=75
    Use text annotation and point to the cluster with the maximum population"""

    df = pd.read_csv("../dataset/titanic.csv",encoding = "ISO-8859-1")
    # drop where no age
    df['Age'] = df['Age'].dropna()

    df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')

    ages = df['Age']
    print(type(df))
    # age group 1 < 25
    ag_1 = ages[ages < 25]
    # age group 25 <= 50
    ag_2 = ages[ages.between(25, 50, inclusive='left')]
    # age group 50 <= 75
    ag_3 = ages[ages.between(50, 75, inclusive='left')]
    # age group 75+
    ag_4 = ages[ages >= 75]

    segments = [len(ag_1), len(ag_2), len(ag_3), len(ag_4)]
    labels = ['< 25', '25 to 50', '50 to 75', '> 75']

    sectionToExplode=(0.2, 0, 0, 0)
    plt.pie(segments, shadow=True, startangle=90, autopct='%0.1f%%', pctdistance=1.1, labeldistance=1.3, labels=labels)
    # plt.legend(patches, labels, loc="best")
    plt.annotate('The largest age cluster', xy=(1, 0), xytext=(1, .5), arrowprops=dict(arrowstyle="->"))
    plt.annotate('The smallest age cluster', xy=(0, 1), xytext=(-1.5, 1), arrowprops=dict(arrowstyle="->"))
    plt.show()

q06()
