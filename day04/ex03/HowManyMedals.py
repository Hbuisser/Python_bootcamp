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

def howManyMedals(df, name):
    main_dico = {}
    dfn = df[df['Name'] == name]
    for elem in dfn['Year']:
        main_dico[elem] = {'G' : 0, 'S' : 0, 'B' : 0}
    for year in main_dico.keys():
        mininew = dfn[dfn['Year'] == year]
        for medal in mininew['Medal']:
            if medal == 'Gold':
                main_dico[year]['G'] += 1
            if medal is 'Silver':
                main_dico[year]['S'] += 1
            if medal is 'Bronze':
                main_dico[year]['B'] += 1
    print(main_dico)

if __name__ == "__main__":
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    howManyMedals(df, 'Kjetil Andr Aamodt')