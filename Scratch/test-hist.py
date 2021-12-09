import pandas as pd
from matplotlib import pyplot as plt
import sys


def Task6():
    """Each movie has a length (duration). Apply an appropriate visualization technique and visually
    depict what durations (movie lengths) are more common and popular among all movies in the file.

    Use comment and indicate the common and popular movie lengths.

    Data Cleansing: Some movies do not have a known duration, those movies (rows) should be
    ignored for this task"""
    movies = pd.read_csv("../dataset/imdbratings.txt")

    print(movies.head())
    # only need the countries
    plt.hist(movies.duration)

    print(movies.duration)
Task6()
