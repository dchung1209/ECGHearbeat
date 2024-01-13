import pandas as pd

class DataUtils():
    def __init__(self, directory):
        self.dir = directory
    
    def get_df(self, train : bool):
        if (train):
            path = self.dir + "/mitbih_train.csv"
        else:
            path = self.dir + "/mitbih_test.csv"

        df = pd.read_csv(path, header = None)
        return df
    
    def get_labels(self, train : bool):
        df = self.get_df(train)
        return df[187]
    
    def clean_df(self, df):
        return df.drop(187, axis = 1)
    
