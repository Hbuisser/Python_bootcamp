import pandas as pd

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

class SpatioTemporalData:
    def __init__(self, df):
        self.df = df

    def when(self, location):
        lst = []
        new = self.df[self.df['City'] == location]
        for year in new['Year'].drop_duplicates():
            lst.append(year)
        return lst

    def where(self, date):
        lst = []
        new = self.df[self.df['Year'] == date]
        for place in new['City'].drop_duplicates():
            lst.append(place)
        return lst

if __name__ == "__main__":
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    stp = SpatioTemporalData(df)
    print(stp.where(1896))
    print(stp.when('Athina'))
    print(stp.when('Paris'))
