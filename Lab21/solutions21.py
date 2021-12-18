import time

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate, train_test_split, KFold
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.svm import SVC
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
    # print(f"Mode: {df['Sex'].mode()}")
    val_high_freq = all_freq[all_freq == high_freq].index[0]
    # print(all_freq[all_freq == high_freq ].index[0])
    df['Sex'] = df['Sex'].fillna(val_high_freq)

    # clean up sex values further
    # print(df['Sex'].value_counts())
    df.loc[df['Sex'] == 'M', 'Sex'] = 1
    df.loc[df['Sex'] == '.', 'Sex'] = 1
    df.loc[df['Sex'] == 'F', 'Sex'] = 2
    # print(df['Sex'].value_counts())
    # print(f"mode: {df['Sex'].mode()}")
    # print(f"value_counts:\n {df['Sex'].value_counts()}")
    # print(f"idxmax: {df['Sex'].value_counts().idxmax()}")

    # clean up fatals
    # for i in df.columns:
    #     print(f"column {i}")
    #
    #     print(df[i].unique())
    #     print(df[i].value_counts(dropna=False))

    df['Fatal'] = df['Fatal'].str.strip()
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

    # print(len(dict_activities))

    X = (df[['Activity', 'Sex']])

    y = df[['Fatal']]

    tree_clf = tree.DecisionTreeClassifier()
    cv = KFold(n_splits=3, random_state=1, shuffle=True)
    # cv_results = cross_validate(tree_clf, X, y, cv=3, scoring='accuracy', return_train_score=True)
    cv_results = cross_validate(tree_clf, X, y, cv=cv, scoring='accuracy', return_train_score=True)

    print('Training  ', cv_results['train_score'].mean())
    print('Training  ', cv_results['train_score'])

    # clf.fit(X_test, y_test)

    print('Testing ....  ', cv_results['test_score'].mean())
    print('Testing ....  ', cv_results['test_score'])


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
    # record = df[df['Fatal'] == "2017"]
    # print(df['Fatal'].value_counts())
    df = df[df['Fatal'] != "2017"]

    # clean activity
    # df['Activity'] = df['Activity'].str.strip()
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
    # df['Country'] = df['Country'].str.strip()
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

    tree_clf = DecisionTreeClassifier(random_state=42)

    tree_clf.fit(X_train, y_train)

    print('Training  ', tree_clf.score(X_train, y_train))

    print('Testing  ', tree_clf.score(X_test, y_test))


def Q2():
    df = pd.read_csv("../dataset/attacks.csv", encoding="ISO-8859-1")

    flt = df[['Activity', 'Country', 'Fatal']].copy()
    flt = flt[['Activity', 'Country', 'Fatal']].dropna()

    all_activities = np.unique(flt['Activity'].astype(str))

    dict2 = {}
    c = 1
    for ac in all_activities:
        dict2[ac] = c
        c = c + 1

    # apply dictionary to Activity column
    flt['Activity'] = flt['Activity'].map(dict2)

    # print(dict2)

    # apply dictionary to Country column
    all_countries = np.unique(flt['Country'].astype(str))

    dict2 = {}
    c = 1
    for ac in all_countries:
        dict2[ac] = c
        c = c + 1

    flt['Country'] = flt['Country'].map(dict2)

    all_fatals = np.unique(flt['Fatal'].astype(str))

    dict1 = {}
    c = 1
    for ac in all_fatals:
        dict1[ac] = c
        c = c + 1

    flt['Fatal'] = flt['Fatal'].map(dict1)
    # print(dict1)

    X = (flt[['Activity', 'Country']])

    y = flt[['Fatal']]

    # get test/training data where we are only using 1% of data for training
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.99, random_state=42)

    # tree_clf = tree.DecisionTreeClassifier( random_state=42)

    # get a DTC model
    tree_clf = DecisionTreeClassifier(random_state=42)

    # fit the model
    tree_clf.fit(X_train, y_train)

    print('Training  ', tree_clf.score(X_train, y_train))
    print('Testing  ', tree_clf.score(X_test, y_test))


def q03():
    """You should first perform the following pre-processing steps in order:
    1. Make all the non numerical cells from Age attribute, empty.
    2. Fill in the empty cells in Age attribute by the average of all existing numerical values in the Age attribute.
    3. Convert the values in the Activity attribute into numerical values as follows:
    a. If a cell contains the term surf (small or capital cases) the value of the cell is converted to 0.
    E.g., (Surfing -> 0) or (Surf fishing -> 0).
    b. If a cell contains the term swim (small or capital cases) the value of the cell is converted to 1.
    E.g., (Swimming -> 1) or (Swimming after falling overboard -> 1)
    c. If a cell contains the term shark (small or capital cases) the value of the cell is converted to 2.
    E.g., (Attempting to free the shark -> 2) or (Fishing for sharks -> 2).
    (See the following code snippet where flt is your customized dataframe):
    d. Make all other cells empty.
    4. Remove all rows that have at least one empty cell.
    5. Convert all categorical values in Fatal attribute to numerical values."""

    col_list = ["Activity", "Age", "Fatal"]
    df = pd.read_csv('../dataset/attacks.csv', usecols=col_list, encoding="ISO-8859-1")

    flt = df.copy()

    # Force all Age values to be numeric
    flt['Age'] = flt['Age'].apply(pd.to_numeric, errors='coerce')

    # Fill in all empty with mean of Age
    flt['Age'] = flt['Age'].fillna(flt['Age'].mean())

    # flt.loc[flt['Activity'].str.lower().str.contains('surf', na=False), 'Activity'] = 0
    # 3. Convert the values in the Activity attribute into numerical values as follows:
    # a. If a cell contains the term surf (small or capital cases) the value of the cell is converted to 0.
    # E.g., (Surfing -> 0) or (Surf fishing -> 0).
    flt.loc[flt['Activity'].str.lower().str.contains('surf', na=False), 'Activity'] = 0

    # b. If a cell contains the term swim (small or capital cases) the value of the cell is converted to 1.
    # E.g., (Swimming -> 1) or (Swimming after falling overboard -> 1)
    flt.loc[flt['Activity'].str.lower().str.contains('swim', na=False), 'Activity'] = 1

    # c. If a cell contains the term shark (small or capital cases) the value of the cell is converted to 2.
    # E.g., (Attempting to free the shark -> 2) or (Fishing for sharks -> 2).
    flt.loc[flt['Activity'].str.lower().str.contains('shark', na=False), 'Activity'] = 3

    # Force non-numeric columns to become NaN
    # d. Make all other cells empty.
    flt['Activity'] = flt['Activity'].apply(pd.to_numeric, errors='coerce')

    # 4. Remove all rows that have at least one empty cell.
    flt = flt.dropna()
    # print(flt.head())

    # 5. Convert all categorical values in Fatal attribute to numerical values."""
    # print(flt['Fatal'].value_counts())
    flt['Fatal'] = flt['Fatal'].str.strip().str.upper()
    flt = flt[flt['Fatal'] != "2017"]
    flt = flt[flt['Fatal'] != "UNKNOWN"]
    # print(flt['Fatal'].value_counts())

    # get a list of unique fatal values
    unique_fatals = np.unique(flt['Fatal'])

    # create a dictionary of fatal values to integer values
    dict_fatals = {}
    c = 1
    for ac in unique_fatals:
        dict_fatals[ac] = c
        c = c + 1

    # map a dictionary to fatal values
    flt['Fatal'] = flt['Fatal'].map(dict_fatals)

    X = (flt[['Activity', 'Age']])

    y = flt[['Fatal']].values.ravel()

    models = []

    models.append(('KNN', KNeighborsClassifier()))
    models.append(('DTC', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC(kernel='linear')))
    models.append(('RFS', RandomForestClassifier()))
    # evaluate each model in turn
    names = []
    results = {}
    for name, model in models:
        start = time.time()

        print(f"Model {name}")
        cv_results = cross_validate(model, X, y, cv=5, scoring='accuracy', return_train_score=True)

        results[name] = cv_results
        # print(cv_results)
        stop = time.time()
        duration = stop - start
        print(duration)

    for models in results:
        print(models)
        print('Training  ', results[models]['train_score'].mean())
        print('Test  ', results[models]['test_score'].mean())


def Q3():
    df = pd.read_csv("../dataset/attacks.csv", encoding="ISO-8859-1")

    flt = df[['Activity', 'Age', 'Fatal']].copy()

    flt['Age'] = flt['Age'].apply(pd.to_numeric, errors='coerce')
    flt['Age'] = flt['Age'].fillna(flt['Age'].mean())

    flt.loc[flt['Activity'].str.lower().str.contains('surf', na=False), 'Activity'] = 0
    flt.loc[flt['Activity'].str.lower().str.contains('swimm', na=False), 'Activity'] = 1
    flt.loc[flt['Activity'].str.lower().str.contains('shark', na=False), 'Activity'] = 2

    flt['Activity'] = flt['Activity'].apply(pd.to_numeric, errors='coerce')

    flt = flt.dropna()
    flt['Fatal'] = flt['Fatal'].str.strip().str.upper()
    flt = flt[flt['Fatal'] != "2017"]
    flt = flt[flt['Fatal'] != "UNKNOWN"]

    allFatals = np.unique(flt['Fatal'])

    dict1 = {}
    c = 1
    for ac in allFatals:
        dict1[ac] = c
        c = c + 1

    print(dict1)
    flt['Fatal'] = flt['Fatal'].map(dict1)

    X = (flt[['Activity', 'Age']])

    y = flt[['Fatal']].values.ravel()

    models = []

    models.append(('KNN', KNeighborsClassifier()))
    models.append(('DTC', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC(kernel='linear')))
    models.append(('RFS', RandomForestClassifier()))
    # evaluate each model in turn
    names = []
    results = {}
    for name, model in models:
        start = time.time()

        print(f"Model {name}")
        cv_results = cross_validate(model, X, y, cv=5, scoring='accuracy', return_train_score=True)

        results[name] = cv_results
        # print(cv_results)
        stop = time.time()
        duration = stop - start
        print(duration)

    for models in results:
        print(models)
        print('Training  ', results[models]['train_score'].mean())
        print('Test  ', results[models]['test_score'].mean())


def q04():
    """Use Age, Pclass and Sex attributes in the titanic and train a decision tree classifier to
    predict Survived.
    Use appropriate visualization technique and determine what is the best value for the
    depth of the decision tree."""
    col_list = ["Age", "Pclass", "Sex", "Survived"]
    df = pd.read_csv("../dataset/titanic.csv", usecols=col_list, encoding="ISO-8859-1")

    flt = df.copy()

    # flt.rename(columns={'Sex ': 'Sex'}, inplace=True)
    print(flt['Sex'].value_counts())

    sex_dict = {'female': 1, 'male': 2}
    flt['Sex'] = flt['Sex'].map(sex_dict)
    flt['Sex'] = flt['Sex'].astype(int)

    print(flt['Sex'].value_counts())

    flt['Age'] = flt['Age'].apply(pd.to_numeric, errors='coerce')
    flt['Age'] = flt['Age'].fillna(flt['Age'].mean())

    print(flt['Pclass'].value_counts())
    print(flt['Survived'].value_counts())

    X = (flt[['Age', 'Pclass', 'Sex']])

    y = flt[['Survived']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    c = 1
    mylistTr = []
    mylistTs = []
    index = range(1, 21)
    for n in range(20):
        clf = tree.DecisionTreeClassifier(max_depth=c, random_state=42)
        c = c + 1
        clf.fit(X_train, y_train)

        # print(clf.score(X_train, y_train))

        mylistTr.append(clf.score(X_train, y_train))
        mylistTs.append(clf.score(X_test, y_test))

    plt.plot(index, mylistTr)
    plt.plot(index, mylistTs)
    plt.legend(['Train', 'Test'])
    plt.show()


def q05():
    """Use titanic and predict the price range of the tickets by a classification algorithm. Use
    Pclass, Sex, Survived for this classification."""
    col_list = ["Pclass", "Sex", "Survived", "Fare"]
    df = pd.read_csv("../dataset/titanic.csv", usecols=col_list, encoding="ISO-8859-1")

    flt = df.copy()
    sex_dict = {'female': 1, 'male': 2}
    flt['Sex'] = flt['Sex'].map(sex_dict)
    flt['Sex'] = flt['Sex'].astype(int)
    flt = flt.dropna()

    print(flt.head(20))

    X = (flt[["Pclass", "Sex", "Survived"]].values)

    y = flt[["Fare"]]
    print(y.value_counts())
    print(y.min())
    print(y.max())

    y = y.dropna()
    y = y.values.reshape(-1, 1)
    enc = KBinsDiscretizer(n_bins=20, encode='ordinal', strategy='uniform')
    # print(enc)
    enc.fit(y)
    y = enc.transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    clf = tree.DecisionTreeClassifier(random_state=42)

    clf.fit(X_train, y_train)

    # print(clf.score(X_train, y_train))

    print(clf.score(X_train, y_train))
    print(clf.score(X_test, y_test))

    # Pclass" p , "Sex" g, "Survived s
    for p in (1, 2, 3):
        for g in (1, 2):
            for s in (0, 1):
                bin_val = clf.predict([[p, g, s]])
                val = enc.inverse_transform(np.array(bin_val).reshape(1, -1))
                print(f"Class: {p}, Sex: {g}, Survived: {s}, Fare: {val[0,0]}")

# q01()
# q02()
# q03()
# q04()
q05()
