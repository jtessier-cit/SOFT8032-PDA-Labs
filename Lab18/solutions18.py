import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def q01():
    """Write a Python program to draw a line with suitable label in the x axis, y axis and
    a title.
    (Hint: axis labels are specified by plt.xlabel('x-label'))
    (Hint: plot title can be inserted by: plt.title('Draw a line.')) (See Figure 1)"""
    x_vals = range(1, 50)
    y_vals = [value *3 for value in x_vals]
    print("Values of X:")
    print(x_vals)
    print("Values of Y:")
    print(y_vals)

    #plot line
    plt.plot(x_vals, y_vals)

    # set axis labels
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Draw a line')
    plt.show()

def q02():
    x_vals = [1, 2, 3]
    y_vals = [2, 4, 0]

    print("Values of X:")
    print(x_vals)
    print("Values of Y:")
    print(y_vals)

    #plot line
    plt.plot(x_vals, y_vals)

    # set axis labels
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Sample Graph')
    plt.show()


def q03():
    """Write a Python program to draw 4 lines for the financial data between October 3,
    2016 to October 7, 2016. (See Figure 3)"""
    df = pd.read_csv("../dataset/fdata.csv", sep=',', parse_dates=True, index_col=0)
    df.plot()
    print(df.index)
    print(df)
    plt.show()

def q04():
    """Write a Python program to plot two or more lines with different styles. (See
    Figure4 )"""
    x1_vals = [10, 20, 30]
    y1_vals = [20, 40, 0]

    x2_vals = [10, 20, 30]
    y2_vals = [40, 0, 30]

    plt.plot(x1_vals, y1_vals, color='blue', linewidth = 3,  label = 'line1-dotted',linestyle=':')
    plt.plot(x2_vals, y2_vals, color='red', linewidth = 2,  label = 'line1-dotted',linestyle='-.')
    # Set a title
    plt.title("Plot with two or more lines with different styles")
    # show a legend on the plot
    plt.legend()
    # function to show the plot

    plt.show()


def q05():
    # Sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # green dashes, blue squares and red triangles
    plt.plot(t, t, 'g--', label="greendash")      #linear, green dashed
    plt.plot(t, t ** 2, 'bs', label="bluesquare")  # squared, blue squares
    plt.plot(t, t ** 3, 'r^', label="redtriangle")  # cubed, red triangle
    plt.legend()
    plt.show()


def q06():
    """Use a plot and show if there is any relationship between the number of survived
    passengers and their class ticket from the titanic file."""
    df = pd.read_csv("../dataset/titanic.csv",encoding = "ISO-8859-1")

    # get boolean for survivors
    bool_survived = df['Survived']==1
    # Get rows where people survived
    survived = df[bool_survived]

    # get all survivors grouped by class
    group_pclass = survived.groupby('Pclass')

    # count entries in survived column
    count_survivors = group_pclass['Survived'].count()

    print(count_survivors)

    count_survivors.plot()
    plt.xticks([1, 2, 3])
    plt.xlabel('Survivors')
    plt.ylabel('Class')
    plt.title('Survivors by Class')
    plt.show()



def q07():
    """Write a Python programming to display a bar chart of the popularity of
    programming Languages. (See Figure 7)"""
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

    plt.bar(x, popularity)
    plt.xlabel('Languages')
    plt.ylabel('Popularity (%)')
    plt.title('Popularity of Programming Language Worldwide\nOct 2017 compared to a year ago')
    plt.show()


def q08a():
    """Use the titanic data set and perform the following tasks:
    a. Create a bar graph to show the number of males and females who have died
    and survived."""
    df = pd.read_csv("../dataset/titanic.csv",encoding = "ISO-8859-1")

    # use only columns we're interested in
    trim_df = df[['Survived']['Sex']]

    # get boolean for survivors
    bool_survived = df['Survived']==1

    # Get rows where people survived
    males = df[bool_survived].groupby('Sex')

def q08b():
    """b. Create a bar graph and show the number of males and females in the age
    range [20, 40]"""

def q08c():
    """c. Use a plot and show the relation between fare and class ticket."""

def q08d():
    """d. Use a pie chart and visualize the population among three different class ticket."""


q07()