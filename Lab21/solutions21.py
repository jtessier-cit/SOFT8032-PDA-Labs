import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.tree import DecisionTreeClassifier


def q01():
    """Use attack dataset to train a decision tree classifier using the following features:
    (Activity type, Gender, Fatality (class attribute)).
    Use 67% of the dataset as training dataset and rest for test.
    Print the average accuracy for both training and test sets for all three folds (iterations):
    Note, ‘Sex’ column has some empty cells, the empty cells need to be filled in with the gender with higher
    frequency; e.g., if there are 2200 M and 3400 F, then empty cells need to be filled in with F"""

    # col_list = ["Activity", "Sex ", "Fatal"]
    #
    # df = pd.read_csv('../dataset/attacks.csv', usecols=col_list, encoding="ISO-8859-1")
    df = pd.read_csv('../dataset/attacks.csv', encoding="ISO-8859-1")
    # print(df.columns)
    # print(df.head().to_string())head
    df.rename(columns={'Sex ': 'Sex'}, inplace=True)
    df['Sex'] = df['Sex'].str.strip()
    df = df[df.Sex != 'lli']
    df.loc[df['Sex'] == 'N', 'Sex'] = "M"

    # print(df.isna().sum())
    df = df[['Activity', 'Sex', 'Fatal', 'Injury']].dropna()
    high_freq = (max(df['Sex'].value_counts()))
    all_freq = df['Sex'].value_counts()
    # print(all_freq)
    val_high_freq = all_freq[all_freq == high_freq ].index[0]
    # print(all_freq[all_freq == high_freq ].index[0])
    df['Sex'] = df['Sex'].fillna(val_high_freq)

    # clean up sex values further
    # print(df['Sex'].value_counts())
    df.loc[df['Sex'] == 'M', 'Sex'] = 1
    df.loc[df['Sex'] == '.', 'Sex'] = 1
    df.loc[df['Sex'] == 'F', 'Sex'] = 2
    # print(df['Sex'].value_counts())

    # clean up fatals
    # for i in df.columns:
    #     print(f"column {i}")
    #
    #     print(df[i].unique())
    #     print(df[i].value_counts(dropna=False))

    df['Fatal'] = df['Fatal'].str.strip()
    record = df[df['Fatal'] == "2017"]
    # print(df['Fatal'].value_counts())
    df = df[df['Fatal'] != "2017"]
    # print(record)
        # print(df.isna().sum())

    # print(df['Fatal'].value_counts())

    df = df[['Activity', 'Sex', 'Fatal']].dropna()
    # print(df.isna().sum())
    # print(df)
    # for i in df.columns:
    #     print(df[i].unique())

    # convert activity to int
    df['Activity'] = df['Activity'].str.strip()
    activities_list = np.unique(df['Activity'].astype(str))

    dict_activities = {}
    c = 1
    for ac in activities_list:
        dict_activities[ac] = c
        c = c + 1

    df['Activity'] = df['Activity'].map(dict_activities)

    print(len(dict_activities))

    X = (df[['Activity', 'Sex']])

    y = df[['Fatal']]

    tree_clf = tree.DecisionTreeClassifier()

    cv_results = cross_validate(DecisionTreeClassifier(), X, y, cv=3, scoring='accuracy', return_train_score=True)

    print('Training  ', cv_results['train_score'].mean())

    # clf.fit(X_test, y_test)

    print('Testing ....  ', cv_results['test_score'].mean())


def q02():
    """In this question we are going to observe the overfitting phenomena.
    Use attack dataset and train a decision tree classifier using the following features: (Activity, Country and
    Fatality (class attribute)). Use only 1% of the dataset as training dataset and the rest for test. Report the
    accuracy for both training and test and discuss your observations. Note that one of the reasons that
    overfitting occurs is the lack of data in our training set"""
    col_list = ["Activity", "Country", "Fatal"]

    df = pd.read_csv('../dataset/attacks.csv', usecols=col_list, encoding="ISO-8859-1")
    print(df.columns)
    df = df.dropna()

    df['Fatal'] = df['Fatal'].str.strip()
    record = df[df['Fatal'] == "2017"]
    # print(df['Fatal'].value_counts())
    df = df[df['Fatal'] != "2017"]


    # clean activity
    df['Activity'] = df['Activity'].str.strip()
    activities_list = np.unique(df['Activity'].astype(str))

    # map activities to integer
    dict_activities = {}
    c = 1
    for ac in activities_list:
        dict_activities[ac] = c
        c = c + 1

    df['Activity'] = df['Activity'].map(dict_activities)
    # print(len(dict_activities))

    # clean country
    df['Country'] = df['Country'].str.strip()
    countries_list = np.unique(df['Country'].astype(str))

    # print(countries_list)
    dict_countries = {}
    c = 1
    for ac in countries_list:
        dict_countries[ac] = c
        c = c + 1

    df['Country'] = df['Country'].map(dict_countries)
    # print(len(dict_activities))

    X = (df[['Activity', 'Country']])

    y = df[['Fatal']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.99, random_state=42)

    tree_clf = DecisionTreeClassifier()

    tree_clf.fit(X_train, y_train)

    print('Training  ', tree_clf.score(X_train, y_train))

    print('Testing  ', tree_clf.score(X_test, y_test))



def Q2():
    df = pd.read_csv("../dataset/attacks.csv", encoding="ISO-8859-1")

    flt = df[['Activity', 'Country', 'Fatal']].copy()

    flt = flt[['Activity', 'Country', 'Fatal']].dropna()

    allActivities = np.unique(flt['Activity'].astype(str))

    dict2 = {}
    c = 1
    for ac in allActivities:
        dict2[ac] = c
        c = c + 1

    flt['Activity'] = flt['Activity'].map(dict2)

    # print(dict2)

    allCountries = np.unique(flt['Country'].astype(str))

    dict2 = {}
    c = 1
    for ac in allCountries:
        dict2[ac] = c
        c = c + 1

    flt['Country'] = flt['Country'].map(dict2)

    allFatals = np.unique(flt['Fatal'].astype(str))

    dict1 = {}
    c = 1
    for ac in allFatals:
        dict1[ac] = c
        c = c + 1

    flt['Fatal'] = flt['Fatal'].map(dict1)
    # print(dict1)

    X = (flt[['Activity', 'Country']])

    y = flt[['Fatal']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.99, random_state=42)

    # tree_clf = tree.DecisionTreeClassifier( random_state=42)

    tree_clf = DecisionTreeClassifier()

    tree_clf.fit(X_train, y_train)

    print('Training  ', tree_clf.score(X_train, y_train))

    print('Testing  ', tree_clf.score(X_test, y_test))


q02()
Q2()
