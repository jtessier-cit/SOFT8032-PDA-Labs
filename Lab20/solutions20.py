import numpy as np
import pandas as pd
from sklearn import tree

def group(df, column, threshold):
    table = df[column].value_counts()
    grouped_columns = [i for i in table.index if table[i] < threshold]
    for n in grouped_columns:
        df.loc[df[column] == n, column] = 'Other'
    print(df[column].value_counts())


def q01():
    """Create a dataset with 400 individuals with three attributes using some random values as follows:
    1. The first feature of the first 200 individual will get a random value in range [10-20]
    2. The second feature of the first 200 individual will get a random value in range [100-200]
    3. The third feature of the first 200 individual will get a fixed value equal to 1
    4. The first feature of the second 200 individual will get a random value in range [15-25]
    5. The second feature of the second 200 individual will get a random value in range [150-250]
    6. The third feature of the second 200 individual will get a fixed value equal to 2
    Use scikitlearn and apply DecisionTreeClassifier, where the features are the first and second columns and
    the class/target attribute is the third column. Train your data and predict the following data individuals:
    (20, 152, ?)
    (10, 110, ?)
    (14, 245, ?)"""


    """1. The first feature of the first 200 individual will get a random value in range [10-20]"""
    #feature1 = (np.random.rand(200) + 1) * 20
    feature1 = np.random.uniform(10, 20, 200)
    # print(feature1)
    """2. The second feature of the first 200 individual will get a random value in range [100-200]"""
    feature2 = np.random.uniform(100, 200, 200)

    """3. The third feature of the first 200 individual will get a fixed value equal to 1"""
    feature3 = np.ones(200)

    """4. The first feature of the second 200 individual will get a random value in range [15-25]"""
    feature1 = np.append(feature1, np.random.uniform(15, 25, 200))

    """5. The second feature of the second 200 individual will get a random value in range [150-250]"""
    feature2 = np.append(feature2, np.random.uniform(150, 250, 200))

    """6. The third feature of the second 200 individual will get a fixed value equal to 2"""
    feature3 = np.append(feature3, np.full(200, 2))

    print(type(feature1))
    # print(feature1)
    # print(feature2)
    # print(feature3)

    clf = tree.DecisionTreeClassifier()
    # all_features = pd.concat([feature1, feature2], axis=1)
    all_features = pd.DataFrame({'feature1': feature1, 'feature2': feature2})
    print(all_features.head(5))

    # feature3 = pd.DataFrame({'feature3': feature3})

    clf.fit(all_features, feature3)
    print(clf.predict([[20, 152]]))
    print(clf.predict([[10, 110]]))
    print(clf.predict([[14, 245]]))
    print(clf.predict([[15, 150]]))  # Typical 1
    print(clf.predict([[20, 200]]))  # Typical 2


def q02():
    # read in the dataframe
    df = pd.read_csv("../dataset/titanic.csv", encoding="ISO-8859-1")

    # Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked

    # reduce the dataframe to pclass, gender and survive
    df = df[['Pclass', 'Sex', 'Survived']]
    # print(df.head(5))

    """ 
       Approach 1 how to deal with categorical data when the number of
       unique categorical values is small and known to us ...
    
    """
    # print(df['Sex'].unique())

    sex_dict = {'female': 1, 'male': 2}
    df['Sex'] = df['Sex'].map(sex_dict)
    df['Sex'] = df['Sex'].astype(int)

    # print(df.head(5))
    # print(df.isna().sum())

    # df = df.dropna()
    # print(df.shape)

    x = df[['Pclass', 'Sex']]
    y = df[['Survived']]

    # print(x.head())
    # print(y.head())
    """ 
    Approach 2 how to deal with categorical data . where we can 
    use conditionas e.g., only chanege cells with values 'male' 
    from column 'Sex' to 2: df.loc[df['Sex']=='male', 'Sex'] = 2
    
    df.loc[df['Sex']=='male', 'Sex'] = 2
    df.loc[df['Sex']=='female', 'Sex'] = 1
    """
    tree_clf = tree.DecisionTreeClassifier()
    tree_clf.fit(x.values, y.values)


    for key, val in sex_dict.items():
        for pclass in [1, 2, 3]:
            print(f"Class: {pclass}, Sex: {key}, Survived: {tree_clf.predict([[pclass, val]])}")
            # print(tree_clf.predict([[pclass, val]]))


def q03():
    """Sckitlearn and decisionTree has another function called clf.score(x, y) where clf is the instance of your
    classifier, x is the attributes of your dataset and y is your class/target attribute. Score() returns the
    accuracy of your model (how good your model has been trained for prediction).
    Use titanic dataset train a model (classification model) and predict whether or not a passenger would
    survive using two different datasets:
    1. Pclass and Age
    2. Pclass, Age and Gender
    Use predict function and try to predict multiple values and discuss which model potentially might be
    more accurate."""
    col_list = ["Pclass", "Age", "Sex", "Survived"]

    df = pd.read_csv("../dataset/titanic.csv", usecols=col_list, encoding="ISO-8859-1")
    print(df.head())

    df.loc[df['Sex'] == 'female', 'Sex'] = 1
    df.loc[df['Sex'] == 'male', 'Sex'] = 2
    print(df.head())
    print(df.isna().sum())
    ## Only Age had na values
    df['Age'] = df['Age'].fillna(value=df['Age'].mean())

    # for Pclass and Age
    X = df[['Pclass', 'Age']]
    y = df[['Survived']]

    tree_clf = tree.DecisionTreeClassifier(random_state=42)
    tree_clf.fit(X.values, y)
    print(tree_clf.score(X, y))

    for p in [1, 2, 3]:
        for a in range(0,100,5):
            print(f"pClass: {p}, age: {a}, {tree_clf.predict([[p, a]])}")
            # print(clf.predict([[10, 110]]))


    importance = tree_clf.feature_importances_
    # summarize feature importance
    for i, v in enumerate(importance):
        print('Feature: %0d, Score: %.5f' % (i, v))


    # for Pclass , Age, Sex
    X = df[['Pclass', 'Age', 'Sex']]
    y = df[['Survived']]

    tree_clf = tree.DecisionTreeClassifier(random_state=42)
    tree_clf.fit(X.values, y)
    print(tree_clf.score(X, y))

    for p in [1, 2, 3]:
        for a in range(0,100,5):
            for s in [1, 2]:
                print(f"pClass: {p}, age: {a}, sex: {s} {tree_clf.predict([[p, a, s]])}")

    importance = tree_clf.feature_importances_
    # summarize feature importance
    for i, v in enumerate(importance):
        print('Feature: %0d, Score: %.5f' % (i, v))


def q04():
    df = pd.read_csv('../dataset/attacks.csv', encoding="ISO-8859-1")
    print(df.head().to_string())
    """
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
    15. Investigator or Source"""
    print(df.info())
    print(df.columns)
    drop_columns = ['Case Number', 'Date', 'Area', 'Location', 'Name', 'Injury', 'Time', 'Species ',
                    'Investigator or Source', 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2',
                    'original order']
    df.drop(drop_columns, axis=1, inplace=True)
    df.rename(columns={'Sex ': 'Sex'}, inplace=True)

    print(df.columns)
    print(df['Type'].unique())
    print(df['Sex'].unique())
    print(df.info())
    df = df.dropna()
    df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')
    print(df['Age'].unique())
    print(df.shape)
    df = df.dropna()
    print(df['Age'].unique())
    print(df['Activity'].value_counts())
    df.loc[df['Activity'].str.contains('surf', case=False, na=False), 'Activity'] = 'Surfing'
    df.loc[df['Activity'].str.contains('boarding', case=False, na=False), 'Activity'] = 'Surfing'
    df.loc[df['Activity'].str.contains('swim', case=False, na=False), 'Activity'] = 'Swimming'
    df.loc[df['Activity'].str.contains('fishing', case=False, na=False), 'Activity'] = 'Fishing'
    df.loc[df['Activity'].str.contains('aquarium', case=False, na=False), 'Activity'] = 'Fishing'
    df.loc[df['Activity'].str.contains('hunt', case=False, na=False), 'Activity'] = 'Fishing'
    df.loc[df['Activity'].str.contains('trap', case=False, na=False), 'Activity'] = 'Fishing'
    df.loc[df['Activity'].str.contains('walk', case=False, na=False), 'Activity'] = 'Swimming'
    df.loc[df['Activity'].str.contains('wading', case=False, na=False), 'Activity'] = 'Swimming'
    df.loc[df['Activity'].str.contains('float', case=False, na=False), 'Activity'] = 'Swimming'
    df.loc[df['Activity'].str.contains('Treading water', case=False, na=False), 'Activity'] = 'Swimming'
    df.loc[df['Activity'].str.contains('pull', case=False, na=False), 'Activity'] = 'Fishing'
    df.loc[df['Activity'].str.contains('pick', case=False, na=False), 'Activity'] = 'Fishing'
    df.loc[df['Activity'].str.contains('bath', case=False, na=False), 'Activity'] = 'Swimming'
    df.loc[df['Activity'].str.contains('diving', case=False, na=False), 'Activity'] = 'Diving'
    df.loc[df['Activity'].str.contains('snorkel', case=False, na=False), 'Activity'] = 'Diving'
    df.loc[df['Activity'].str.contains('photo', case=False, na=False), 'Activity'] = 'Photo shoot'
    df.loc[df['Activity'].str.contains('film', case=False, na=False), 'Activity'] = 'Filming'
    df.loc[df['Activity'].str.contains('float', case=False, na=False), 'Activity'] = 'Floating'
    df.loc[df['Activity'].str.contains('boarding', case=False, na=False), 'Activity'] = 'Boarding'
    df.loc[df['Activity'].str.contains('wash', case=False, na=False), 'Activity'] = 'Washing'


    print(df['Activity'].value_counts().to_string())

    df['Sex'] = df['Sex'].str.strip()
    df = df[df.Sex != 'lli']

    print(df['Sex'].value_counts())
    df.loc[df['Sex'] == 'M', 'Sex'] = 1
    df.loc[df['Sex'] == 'F', 'Sex'] = 2
    print(df['Sex'].value_counts())


    print(df.shape)

    group(df, 'Activity', 4)
    # for i in df.columns:
    #     print(df[i].unique())
    print(df['Activity'].value_counts().to_string())

    print(df.info())

    """
     Use .astype(str) to make sure all values are treated as string for converstion.
     """
    flt = df
    allActivities = np.unique(flt['Activity'].astype(str))

    dict2 = {}
    c = 1
    for ac in allActivities:
        dict2[ac] = c
        c = c + 1

    flt['Activity'] = flt['Activity'].map(dict2)

    print(dict2)

    allFatals = np.unique(flt['Fatal'])

    dict1 = {}
    c = 1
    for ac in allFatals:
        dict1[ac] = c
        c = c + 1

    flt['Fatal'] = flt['Fatal'].map(dict1)
    print(dict1)

    X = (flt[['Activity', 'Age']])

    y = flt[['Fatal']]
    # print(np.shape(X), np.shape(y))

    tree_clf = tree.DecisionTreeClassifier()
    tree_clf.fit(X, y)
    print(tree_clf.score(X, y))
    # print(df.info())

    importance = tree_clf.feature_importances_
    # summarize feature importance
    for i, v in enumerate(importance):
        print('Feature: %0d, Score: %.5f' % (i, v))

    X = (flt[['Activity', 'Age', 'Sex']])

    y = flt[['Fatal']]
    # print(np.shape(X), np.shape(y))

    tree_clf = tree.DecisionTreeClassifier()
    tree_clf.fit(X, y)
    print(tree_clf.score(X, y))
    # print(df.info())

    importance = tree_clf.feature_importances_
    # summarize feature importance
    for i, v in enumerate(importance):
        print('Feature: %0d, Score: %.5f' % (i, v))


def q05a():
    col_list = ["Age", "Activity", "Fatal"]

    df = pd.read_csv('../dataset/attacks.csv', usecols=col_list, encoding="ISO-8859-1")
    print(df.head().to_string())


    print(df.info())

    print(df.columns)
    df = df.dropna()

    df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')


    df = df[df['Age']<50]

    #
    #
    # print(df['Activity'].value_counts().to_string())


    df['Fatal'] = df['Fatal'].str.strip()
    df['Fatal'] = df['Fatal'].str.lower()


    # group(df, 'Activity', 4)
    # for i in df.columns:
    #     print(df[i].unique())
    print(df['Activity'].value_counts().to_string())

    print(df.info())

    """
     Use .astype(str) to make sure all values are treated as string for converstion.
     """
    flt = df
    allActivities = np.unique(flt['Activity'].astype(str))

    dict2 = {}
    c = 1
    for ac in allActivities:
        dict2[ac] = c
        c = c + 1

    flt['Activity'] = flt['Activity'].map(dict2)

    print(dict2)

    allFatals = np.unique(flt['Fatal'])

    dict1 = {}
    c = 1
    for ac in allFatals:
        dict1[ac] = c
        c = c + 1

    flt['Fatal'] = flt['Fatal'].map(dict1)
    print(dict1)

    X = (flt[['Activity', 'Age']])

    y = flt[['Fatal']]
    # print(np.shape(X), np.shape(y))

    tree_clf = tree.DecisionTreeClassifier()
    tree_clf.fit(X, y)
    # print(tree_clf.score(X, y))
    # print(df.info())

    X = (flt[['Activity', 'Age']])

    y = flt[['Fatal']]
    # print(np.shape(X), np.shape(y))

    tree_clf = tree.DecisionTreeClassifier()
    tree_clf.fit(X, y)
    return(tree_clf.score(X, y))


def q05b():
    df = pd.read_csv("../dataset/attacks.csv", encoding="ISO-8859-1")

    flt = df[['Injury', 'Age', 'Fatal']].copy()

    flt['Age'] = flt['Age'].apply(pd.to_numeric, errors='coerce')

    flt = flt[['Injury', 'Age', 'Fatal']].dropna()
    flt = flt[flt['Age'] < 50]
    # print(np.shape(flt))

    allActivities = np.unique(flt['Injury'].astype(str))
    # print(df['Injury'].value_counts())
    dict2 = {}
    c = 1
    for ac in allActivities:
        dict2[ac] = c
        c = c + 1

    flt['Injury'] = flt['Injury'].map(dict2)

    # print(dict2)

    allFatals = np.unique(flt['Fatal'].astype(str))

    dict1 = {}
    c = 1
    for ac in allFatals:
        dict1[ac] = c
        c = c + 1

    flt['Fatal'] = flt['Fatal'].map(dict1)
    # print(dict1)

    X = (flt[['Injury', 'Age']])

    y = flt[['Fatal']]
    # print(np.shape(X), np.shape(y))

    tree_clf = tree.DecisionTreeClassifier()
    tree_clf.fit(X, y)
    return tree_clf.score(X, y)



def q05():
    print(q05a())
    print(q05b())

q05()