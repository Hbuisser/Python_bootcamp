import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

class FileLoader:
    def load(self, path):
        data = pd.read_csv(path)
        size = data.shape
        print("Loading dataset of dimension {}x{}".format(size[0], size[1]))
        return data

    def display(self, df, n):
        if n >= 0:
            print(df.head(n))
        elif n < 0:
            print(df.tail(n * -1))

class MyPlotLib:
    def histogram(self, data, features):
        pass
    def density(self, data, features):
        pass
    def pair_plot(self, data, features):
        pass
    def box_plot(self, data, features):
        pass

if __name__ == "__main__":
    kwargs = dict(alpha=0.8, bins=10)
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)

    x = df['Height']
    y = df['Weight']

    # test = plt.hist(x, bins= 10, color='b')
    # plt.gca().set(title='Height')
    # fig, axes = plt.subplots(1, 2, figsize=(10, 3), dpi=100)
    # sns.distplot(x , bins=10, color="blue", ax=axes[0], axlabel='Height')
    # sns.distplot(y , bins=10, color="blue", ax=axes[1], axlabel='Weight')
    n_bins = 10

    fig, axes = plt.subplots(nrows=1, ncols=2)
    ax0, ax1= axes.flatten()

    ax0.hist(x, **kwargs, density=True, histtype='bar', color='b')
    ax0.set_title('Height')
    ax0.grid()

    ax1.hist(y, **kwargs, density=True, histtype='bar', color='b')
    ax1.set_title('Weight')
    ax1.grid()

    plt.show()