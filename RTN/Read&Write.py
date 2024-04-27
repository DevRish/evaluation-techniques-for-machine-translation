import pandas as pd

class ReadnWrite:
    def __init__(self):
        self.df = pd.read_csv("C:/Users/ghosh/PycharmProjects/pythonProject/Datasheet - Sheet1.csv")

    def read(self):
        references = self.df["Reference Text "]
        candidates = self.df["Candidate Text"]
        refcanddict = {r: [c for c in candidates ]}
