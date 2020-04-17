import pandas as pd
import numpy as np

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

def proportionBySport(df, year, sport, gender):
    dfy = df[df['Year'] == year].drop_duplicates('Name')
    dfg = dfy[dfy['Sex'] == gender]
    dfs = dfg[dfg['Sport'] == sport]
    dfy2 = df[df['Year'] == year].drop_duplicates('Name')
    dfg = dfy2[dfy2['Sex'] == gender]
    res = float(dfs.shape[0]) / float(dfg.shape[0])
    print(res)


if __name__ == "__main__":
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    proportionBySport(df, 2004, 'Tennis', 'F')