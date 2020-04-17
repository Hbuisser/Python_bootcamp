import pandas as pd
import numpy as np

class FileLoader:
    def load(path):
        data = pd.read_csv(path)
        size = .shape
        print("Loading dataset of dimension {}x{}".format(data[0], data[1]))
    def display(df, n):
        pass
    
if __name__ == "__main__":
    path = "athlete_events.csv"
    fl = FileLoader()
    dt = fl.load(path)
    print(dt)