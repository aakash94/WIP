import os

import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

from collections import OrderedDict, defaultdict
from matplotlib import pyplot as plt
from FetchGrammy import FetchGrammy


def set_sns_theme():
    sns.set_theme(style="darkgrid", font='Latin Modern Roman')
    #sns.set_palette("husl")



def plot_dict(a, tag=""):
    od = OrderedDict(sorted(a.items()))
    plt.bar(range(len(od)), od.values())
    plt.title(tag)
    plt.show()


def plot_list(a, tag=""):
    plt.bar(range(len(a)), a)
    plt.title(tag)
    plt.show()


def plot_gender_representation(df: pd.DataFrame):
    df = df.filter(['year', 'gender'], axis=1)
    df.loc[df['gender'] == 'Unknown', 'gender'] = 'Group'
    # a = df.groupby(['year']).count()
    ser = df.groupby(['year']).value_counts()

    f = defaultdict(int)
    m = defaultdict(int)
    g = defaultdict(int)
    for a in ser.iteritems():
        ((y, s), c) = a
        if s == 'Male':
            m[y] += c
        if s == 'Female':
            f[y] += c
        if s == 'Group':
            g[y] += c

        m[y] += 0
        f[y] += 0
        g[y] += 0

    # print(ser)
    # print(m)
    # print(f)
    # print(g)
    # plot lines
    plt.plot(m.keys(), m.values(), label="Male")
    plt.plot(f.keys(), f.values(), label="Female")
    plt.plot(g.keys(), g.values(), label="Groups")
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()


def plot_lyrical_happiness(df: pd.DataFrame):
    df = df.filter(['year', 'gender', 'sentiment'], axis=1)
    df.loc[df['gender'] == 'Unknown', 'gender'] = 'Group'
    # a = df.groupby(['year']).count()
    ser = df.groupby(['year', 'gender']).mean()
    print(ser)

    f = defaultdict(int)
    m = defaultdict(int)
    g = defaultdict(int)
    for b in ser.iteritems():
        a2 = b[1]

        for a in a2.iteritems():
            ((y, s), c) = a
            if s == 'Male':
                m[y] += c
            if s == 'Female':
                f[y] += c
            if s == 'Group':
                g[y] += c

            m[y] += 0
            f[y] += 0
            g[y] += 0

    # print(ser)
    # print(m)
    # print(f)
    # print(g)
    # plot lines
    plt.plot(m.keys(), m.values(), label="Male")
    plt.plot(f.keys(), f.values(), label="Female")
    plt.plot(g.keys(), g.values(), label="Groups")
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()


def main():
    set_sns_theme()
    fg = FetchGrammy()
    records = fg.load_tsv()
    # plot_gender_representation(df=records)
    plot_lyrical_happiness(df=records)


if __name__ == '__main__':
    main()
