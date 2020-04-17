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

def howManyMedalsByCoutry(dt, country):
    new = df[df['Team'] == country]
    new_dico = {}
    for games in new['Games']:
         new['Medal'].drop_duplicates()
    for year in new['Year'] :
        new_dico[year] = {'G': 0, 'S': 0, 'B': 0}
    for year in new_dico.keys() :
        mininew = new[new['Year'] == year]
        for medal in mininew['Medal'] :
            if medal == 'Gold' :
                new_dico[year]['G'] += 1
            if medal == 'Silver' :
                new_dico[year]['S'] += 1
            if medal == 'Bronze' :
                new_dico[year]['B'] += 1
    print(new_dico)

if __name__ == "__main__":
    path = "athlete_events.csv"
    fl = FileLoader()
    df = fl.load(path)
    stp = howManyMedalsByCoutry(df, 'Norway')