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
        def histogram(self, data, features):
            fig, axes = plt.subplots(nrow=1, ncol=len(features))
            for ft in features :
                ft = axes.flatten()
                lst = list(data[ft])
                arr = np.array([x for x in lst if ~np.isnan(x)])
                ft.hist(arr, bins=8)
                ft.set_tittle(ft)
                ft.grid()
            plt.show()
    def density(self, data, features):
        pass
    def pair_plot(self, data, features):
        pass
    def box_plot(self, data, features):
        pass

if __name__ == "__main__":
    # kwargs = dict(alpha=0.8, bins=10)
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)

    # x = df['Height']
    # y = df['Weight']

    features = ['Height', 'Weight']
    test = MyPlotLib()
    test.histogram(df, features)

    # fig, axes = plt.subplots(nrows=1, ncols=2)
    # ax0, ax1= axes.flatten()

    # ax0.hist(x, **kwargs, density=True, histtype='bar', color='b')
    # ax0.set_title('Height')
    # ax0.grid()

    # ax1.hist(y, **kwargs, density=True, histtype='bar', color='b')
    # ax1.set_title('Weight')
    # ax1.grid()

    #plt.show()