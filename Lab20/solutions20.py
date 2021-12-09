import numpy as np
import pandas as pd
from sklearn import tree


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
    all_features = pd.concat([feature1, feature2], axis=1)
    print(all_features.head(5))
    # all_features = pd.DataFrame({'feature1': feature1, 'feature2': feature2})

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
    print(df.head(5))

    """ 
       Approach 1 how to deal with categorical data when the number of
       unique categorical values is small and known to us ...
    
    """

    sex_dict = {'female': 1, 'male': 2}
    df['Sex'] = df['Sex'].map(sex_dict)
    df['Sex'] = df['Sex'].astype(int)

    print(df.head(5))
    # print(df.isna().sum())

    # df = df.dropna()
    # print(df.shape)

    x = df[['Pclass', 'Sex']]
    y = df[['Survived']]

    print(x.head())
    print(y.head())
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
    tree_clf.fit(X, y)
    print(tree_clf.score(X, y))

    # for Pclass , Age, Sex
    X = df[['Pclass', 'Age', 'Sex']]
    y = df[['Survived']]

    tree_clf = tree.DecisionTreeClassifier(random_state=42)
    tree_clf.fit(X, y)
    print(tree_clf.score(X, y))

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

    print(df['Type'].unique())
    # for i in df.columns:
    #     print(df[i].unique())

q04()