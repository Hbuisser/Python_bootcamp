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

def youngestFellah(df, year):
    new_dic = {}
    test = df.loc[df['Year'] == year]
    new_dic['f'] = test['Age'].loc[df['Sex'] == 'M'].min()
    new_dic['m'] = test['Age'].loc[df['Sex'] == 'F'].min()
    print (new_dic)
    # test = df.loc[df['Year'] == year]
    # testF = test.loc[test['Sex'] == 'F']
    # testF = testF['Age'].min()
    # testM = test.loc[test['Sex'] == 'M']
    # testM = testM['Age'].min()
    # print(testF)
    # print(testM)
    # new_dic = {}
    # new_dic['f'] = testF
    # new_dic['m'] = testM
    # print(new_dic)

    new_dic = {}
    new_dic['f'] = testF
    new_dic['m'] = testM
    print(new_dic)

if __name__ == "__main__":
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    youngestFellah(df, 2000)
