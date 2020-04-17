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


if __name__ == "__main__":
    path = "athlete_events.csv"
    fl = FileLoader()
    dt = fl.load(path)
    fl.display(dt, 12)
    # print(dt)