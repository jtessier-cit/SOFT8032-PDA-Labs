"""
For each of the following questions you will use a dataset containing information on global
shark attacks.

Attribute Information:
The attributes recorded in the dataset are as follows:
0. Case Number
1. Date
2. Year
3. Type
4. Country
5. Area
6. Location
7. Activity
8. Name
9. Sex
10. Age
11. Injury
12. Fatal (Y/N)
13. Time
14. Species
15. Investigator or Source
"""

import pandas as pd

# import data into dataframe
# attaches is ISO-8859-1 encoded
df = pd.read_csv('../dataset/attacks.csv', encoding="ISO-8859-1")


def q01():
    """Using Groupby function write a program that can calculate the average age for each single country.
    """

    # age ends up being non-numeric for some reason
    df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')
    ages = df.groupby('Country')['Age'].isnull()
    print(ages.head(100).to_string())


def q02():
    """Some countries in the attack csv file have multiple different areas, e.g.,
    AUSTRALIA New South Wales
    AUSTRALIA Victoria
    ….
    Write a function that can count the number of different areas for each country and print the name of the
    country along with the number of different areas mentioned in the file."""

    # some countries have leading or preceding spaces
    df['Country'] = df['Country'].str.strip()
    # some areas have leading or preceding spaces
    df['Area'] = df['Area'].str.strip()

    grouped_df = df.groupby("Country")
    grouped_df = grouped_df.agg({'Area': 'nunique'})

    print(grouped_df.to_string())
    print(grouped_df)


def q03():
    """There are some cells in the attack file with no value (empty, NaN). Repeat the previous question and this
    time, for each country, only count the number of different areas where the area has an actual value (no
    empty cell should be considered)."""
    df = pd.read_csv('../dataset/attacks.csv', encoding="ISO-8859-1")

    # some countries have leading or preceding spaces
    df['Country'] = df['Country'].str.strip()
    # some areas have leading or preceding spaces
    df['Area'] = df['Area'].str.strip()

    df = df.dropna(subset=['Area'])
    grouped_df = df.groupby("Country")
    grouped_df = grouped_df.agg({'Area': 'nunique'})
    print(grouped_df.to_string())
    print(grouped_df)


# q03()


def Q2():
    df = pd.read_csv('../dataset/attacks.csv', encoding="ISO-8859-1")
    countryArea = pd.unique(df['Country'])
    for c in countryArea:
        cn1 = df['Country'] == c
        cn = df[cn1]
        areas = pd.unique(cn['Area'])
        print(c, len(areas))


def Q3():
    df = pd.read_csv('../dataset/attacks.csv', encoding="ISO-8859-1")
    countryArea = pd.unique(df['Country'])
    for c in countryArea:
        cn1 = df['Country'] == c
        cn = df[cn1]
        cn = cn.dropna(subset=['Area'])
        areas = pd.unique(cn['Area'])
        print(c, len(areas))


def q05():
    """Question 5.
    Write a program that will show the number of fatal attacks for each country using groupby"""
    df = pd.read_csv('../dataset/attacks.csv', encoding="ISO-8859-1")
    # some countries have leading or preceding spaces
    df['Country'] = df['Country'].str.strip()

    # get a bool for fatal
    b_fatal = df['Fatal'] == "Y"
    all_fatal = df[b_fatal]

    country_fatal = all_fatal.groupby("Country")['Fatal'].size()
    print(country_fatal.to_string())


def q06():
    """Write a program that calculates the average age for each year. Note that some cells contain noises, for
    instance, some cells are empty or some contain an extra space or some contain non-numerical value. You
    first need to clean the required columns and then calculate the average and sort them based on the
    average age. The following lines show you how to clean a column:"""

    # read in dataaset
    df = pd.read_csv('../dataset/attacks.csv', encoding="ISO-8859-1")

    # change age to numeric only
    df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')
    # drop na for age
    df = df.dropna(subset=['Age'])

    group_yrs = df.groupby('Year')
    average_year = group_yrs['Age'].mean()
    sorted_average = average_year.sort_values(ascending=False, na_position='last')
    print(sorted_average.head(10))
    print(sorted_average.tail(10))


def Q6():
    df = pd.read_csv('../dataset/attacks.csv', encoding="ISO-8859-1")

    df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')
    df = df.dropna(subset=['Age'])

    yrs = df.groupby('Year')
    averg = yrs['Age'].mean()
    # averg = averg.dropna()

    print(averg.sort_values().tail(10))

q06()
Q6()
